import io
import re

from read_config import (
	get_trash_words,
	get_typedefs
)
from constants import (
	ENDL,
	NUMS,
	CODING,
	REPLACER,
	COMMENTS,
	MACROSES,
	USELESS_STUFF
)
from formating import format_header_line


def dealias_text(text, config_folder):
	replacements = {alias: name for alias, name in get_typedefs(config_folder)}
	pattern = re.compile(
		'|'.join(
			re.escape(alias) for alias in replacements
		)
	)
	return pattern.sub(lambda x: replacements[x.group(0)], text).strip()


def remove_trash(text, config_folder):
	pattern = re.compile(
		'|'.join(
			re.escape(w) for w in get_trash_words(config_folder)
		)
	)
	return pattern.sub('', text).strip()


def clean_text(text):
	return re.sub(
		r'\s+', ' ',
		(
			text
			.replace('\t', ' ').replace('\n', ' ').replace('\r', '')
			.replace('unsigned', REPLACER).replace('signed', '').replace(REPLACER, 'unsigned')
		)
	).strip()


def normalize_brackets(text):
	return re.sub(
		r'\s+', ' ',
		(
			text
			.replace(' ( ', '(').replace('( ', '(').replace(' (', '(')
			.replace(' ) ', ')').replace(') ', ')').replace(' )', ')')
			.replace(' [ ', '[').replace('[ ', '[').replace(' [', '[')
			.replace(' ] ', ']').replace('] ', ']').replace(' ]', ']')
			.replace(' { ', '{').replace('{ ', '{').replace(' {', '{')
			.replace(' } ', '}').replace('} ', '}').replace(' }', '}')
		)
	).strip()


def normalize_symbols(text):
	l = re.sub(
		r'\s+', ' ',
		(
			text
			.replace(' # ', '#').replace('# ', '#').replace(' #', '#')
			.replace(' , ', ',').replace(', ', ',').replace(' ,', ',')
			.replace(' * ', '*').replace('* ', '*').replace(' *', '*')
			.replace(' & ', '&').replace('& ', '&').replace(' &', '&')
		)
	).strip()
	if '*' in l:
		l = re.sub(
			r'\s+', ' ', 
			re.sub(
				r'(\*+)', r'\1 ', re.sub(r' (\*+)', r'\1 ', l.replace('* *', '**'))
			)
		).strip()
	if '&' in l:
		l = re.sub(
			r'\s+', ' ', 
			re.sub(
				r'(&+)', r'\1 ', re.sub(r' (&+)', r'\1 ', l.replace('& &', '&&'))
			)
		).strip()
	return l


def get_valuable_text(file_):
	for line in file_:
		l = line.strip()
		if any((
			any(l.startswith(n) for n in NUMS),
			any(l.startswith(c) for c in COMMENTS),
			any(l.startswith(m) for m in MACROSES),
			any(l.startswith(u) for u in USELESS_STUFF),
		)):
			yield ''
		else:
			yield format_header_line(l)


def get_text(filepath, config_folder):
	with io.open(filepath, 'r', encoding=CODING) as f:
		text = ENDL.join(t for t in get_valuable_text(f) if t)
	return normalize_brackets(
		normalize_symbols(
			clean_text(
				remove_trash(
					dealias_text(text, config_folder), config_folder
				)
			)
		)
	)
