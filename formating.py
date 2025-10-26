import os
import re

from functools27 import lru_cache
from constants import PLATFORM


@lru_cache()
def format_path(path):
	p = (
		''.join(c for c in path if c not in '\r\n\t\'\"')
		.replace('\\', '/')
		.replace('//', '/')
	).strip()
	if p.startswith('~'):
		login = os.getenv('username')
		home = '/home/%s' % login if not PLATFORM == 'win32' else "C:/Users/%s" % login
		p = (
			p.replace('~', home)
			.replace('//', '/')
		).strip()
	if p.endswith('/'):
		return p[:-1].strip()
	return p


def format_header_line(line):
	l = re.sub(
		r'\s+', ' ',
		''.join(c for c in line.strip() if c not in '\n\r\t')
	).strip()
	if '//' == l or l.startswith('//') or l.startswith('/*') or l.startswith('*/'):
		return ''
	if '//' in l:
		ind = l.rfind('//')
		l = l[:ind].strip()
	if '/*' in l:
		ind = l.rfind('/*')
		l = l[:ind].strip()
	if '*/' in l:
		ind = l.rfind('*/')
		l = l[:ind].strip()
	return l


def format_text_line(line):
	return re.sub(
		r'\s+', ' ', ''.join(c for c in line if c not in '\r\t\n')
	).strip()
