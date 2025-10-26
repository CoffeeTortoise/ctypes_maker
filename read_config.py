import io
import re

from formating import format_path
from constants import CODING, USE_FILENAME


def read_usefile(folder_p, use_filename):
	use_file = format_path('%s/%s' % (folder_p, use_filename))
	with io.open(use_file, 'r', encoding=CODING) as f:
		for filename in f:
			yield format_path(
				'%s/%s' % (
					folder_p, ''.join(c for c in filename if c not in '\r\n\t\'\"; ').strip()
				)
			)


def get_trash_words(config_folder):
	trash_words_p = '%s/TrashWords' % config_folder
	for filepath in read_usefile(trash_words_p, USE_FILENAME):
		with io.open(filepath, 'r', encoding=CODING) as words_file:
			for line in words_file:
				yield ''.join(c for c in line if c not in '\r\n\t\'\"; ')


def get_typedefs(config_folder):
	typedef_p = '%s/Typedefs' % config_folder
	for filepath in read_usefile(typedef_p, USE_FILENAME):
		with io.open(filepath, 'r', encoding=CODING) as defs_file:
			for line in defs_file:
				l = re.sub(
					r'\s+', ' ', ''.join(c for c in line if c not in '\r\t\n\'\";')
				).strip()
				alias, name = l.split('=')
				yield alias.strip(), name.strip()
