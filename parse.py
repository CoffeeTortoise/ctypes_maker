import re

from constants import TYPES_TABLE, ENDL
from formating import format_text_line


def parse_array(line):
	cnt_o, cnt_c = line.count('['), line.count(']')
	if cnt_o != cnt_c:
		return None
	ind = line.find('[')
	type_name = line[:ind].strip()
	ind = type_name.rfind(' ')
	type_, name = type_name[:ind].strip(), type_name[ind + 1:].strip()
	ctype = type_ if type_ not in TYPES_TABLE else TYPES_TABLE[type_]
	dims = (
		line
		.replace(type_name, '')
		.replace('[', ' ')
		.replace(']', ' ')
		.strip()
		.split(' ')
	)
	dims = [d for d in dims if d and d.isdigit()]
	if not dims:
		return None
	j = len(dims) - 1
	while j >= 0:
		ctype = '(%s * %s)' % (ctype, dims[j])
		j -= 1
	return name, ctype


def parse_pointer(line):
	ind = line.rfind(' ')
	type_, name = line[:ind].strip(), line[ind + 1:].strip()
	true_type = 'void*' if 'void*' in type_ else type_.replace('*', '').strip()
	ctype = true_type if true_type not in TYPES_TABLE else TYPES_TABLE[true_type]
	star_cnt = type_.replace(true_type, '').count('*')
	while star_cnt > 0:
		ctype = 'ctypes.POINTER(%s)' % ctype
		star_cnt -= 1
	return name, ctype


def parse_var(line):
	if '[' in line:
		return parse_array(line)
	if '*' in line:
		return parse_pointer(line)
	if '&' in line:
		return parse_pointer(line.replace('&', '*'))
	ind = line.rfind(' ')
	type_, name = line[:ind].strip(), line[ind + 1:].strip()
	ctype = type_ if type_ not in TYPES_TABLE else TYPES_TABLE[type_]
	return name, ctype


def parse_macro(line):
	parts = re.sub(
		r'\s+', ' ', line.replace('#define', '')
	).strip().split(' ')
	if len(parts) != 2:
		return None
	return '%s = %s' % (parts[0].strip(), parts[1].strip())


def parse_constant(line):
	parts = line.split('=')
	if len(parts) != 2:
		return None
	name_type = parse_var(parts[0].strip())
	if name_type is None:
		return None
	return '%s = %s(%s)' % (name_type[0], name_type[1], parts[1].strip())


def parse_enum_var(l, numerator):
	if '=' in l:
		parts = l.split('=')
		if len(parts) != 2:
			return numerator, None
		else:
			name, value = parts[0].strip(), parts[1].replace(',', '').strip()
			if value.isdigit():
				numerator = int(value)
			return numerator, '%s = %s' % (name, value if not ('\'' in value or '\"' in value) else 'ord(%s)' % value)
	else:
		if l.endswith(','):
			name, value = l[:-1].strip(), numerator
			return numerator + 1, '%s = %s' % (name, value)
	return numerator, None


def parse_struct(lines, j):
	l, fields = format_text_line(lines[j]), []
	name = l.replace('typedef', '').replace('struct', '').replace('{', '').replace(' ', '').strip()
	j += 1
	while j < len(lines) and not ('}' in l and ';' in l):
		l = format_text_line(lines[j])
		j += 1
		if not l or not l.endswith(';'):
			continue
		if ',' in l:
			parts = [p.strip() for p in l[:-1].split(',') if p]
			if not parts:
				continue
			name_ctype = parse_var(parts[0])
			if name_ctype is None:
				continue
			fields.append('(\'%s\', %s),' % name_ctype)
			[fields.append('(\'%s\', %s),' % (name, name_ctype[1])) for name in parts[1:] if name]
		else:
			name_ctype = parse_var(l[:-1])
			if name_ctype is None:
				continue
			fields.append('(\'%s\', %s),' % name_ctype)
	structure = ''.join(
		[
			'class %s(ctypes.Structure):\n\t' % name,
			'_fields_ = [\n\t\t', '\n\t\t'.join(fields), '\n\t]'
		]
	)
	return j, structure


def parse_union(lines, j):
	j, structure = parse_struct(lines, j)
	return j, structure.replace('union', '').replace('ctypes.Structure', 'ctypes.Union').strip()


def parse_func_args(func_args):
	for arg in func_args.replace('(', '').replace(')', '').split(','):
		if not arg:
			continue
		yield parse_var(arg)


def create_func_doc(res_type, arg_name_type):
	return '\n\t'.join(
		[
			'\t\'\'\'\n\tArgs:',
			'\t' + '\n\t\t'.join('%s: %s' % (name, type_) for name, type_ in arg_name_type.items()),
			'Returns:\n\t\t%s' % res_type,
			'\'\'\''
		]
	)


def create_func(name, res_type, arg_name_type):
	argtypes = ', '.join(arg_name_type.values())
	argnames = ', '.join(arg_name_type.keys())
	return '\n'.join(
		[
			'DLL_NAME.%s.restype = %s' % (name, res_type),
			'DLL_NAME.%s.argtypes = [%s]\n' % (name, argtypes),
			'def %s(%s):\t' % (name, argnames),
			create_func_doc(res_type, arg_name_type),
			'\treturn DLL_NAME.%s(%s)\n\n' % (name, argnames)
		]
	)


def parse_func(line):
	cnt_o, cnt_c = line.count('('), line.count(')')
	if cnt_o != cnt_c:
		return None
	ind = line.rfind('(')
	type_name, args = line[:ind].strip(), line[ind:].strip()
	ind = type_name.rfind(' ')
	type_, name = type_name[:ind].strip(), type_name[ind + 1:].strip()
	if not name:
		return None
	_, res_type = parse_var('%s dummy' % type_)
	arg_name_type = {name: type_ for name, type_ in parse_func_args(args)}
	return create_func(name, res_type, arg_name_type)


def parse(text):
	lines = [l for l in text.split(ENDL) if l]
	j = 0
	while j < len(lines):
		l = format_text_line(lines[j])
		if l.startswith('#define'):
			yield parse_macro(l)
		elif '=' in l and l.endswith(';'):
			yield parse_constant(l[:-1])
		elif 'enum' in l:
			numerator = 0
			while j < len(lines) and not ('}' in l and ';' in l):
				j += 1
				if j >= len(lines):
					break
				numerator, res = parse_enum_var(l, numerator)
				yield res
				l = format_text_line(lines[j])
		elif 'struct' in l:
			j, res = parse_struct(lines, j)
			yield res
		elif 'union' in l:
			j, res = parse_union(lines, j)
			yield res
		elif '(' in l and ')' in l and l.endswith(';'):
			yield parse_func(l[:-1])
		elif '(' in l:
			buf = [l]
			while j < len(lines) and not ';' in l:
				j += 1
				if j >= len(lines):
					break
				l = format_text_line(lines[j])
				buf.append(l)
			yield parse_func(
				''.join(c.strip() for c in buf if c)[:-1]
			)
		j += 1
