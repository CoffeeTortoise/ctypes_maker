import argparse
import os
import io

from formating import format_path
from get_text import get_text
from constants import CODING
from parse import parse


def create_ctypes(config_folder, in_file, out_file):
	text = get_text(in_file, config_folder)
	with io.open(out_file, 'w', encoding=CODING) as f:
		f.write(
			'\n'.join(r for r in parse(text) if r)
		)
	print 'ctypes wrapper for %s created at %s!' % (in_file, out_file)


def do_stuff(parser_args):
	config_folder = './config' if parser_args.config_folder is None else parser_args.config_folder
	conf, in_f = format_path(config_folder), format_path(parser_args.in_file)
	if not os.path.isdir(conf):
		print '%s doesn\'t exists or not a folder!' % conf
		return
	if not os.path.isfile(in_f):
		print '%s doesn\'t exists or not a file!' % in_f
		return
	if parser_args.out_file is None:
		fname = in_f.split('/')[-1].split('.')[0]
		out_file = './%s.py' % fname
	else:
		out_file = parser_args.out_file
	create_ctypes(config_folder, in_f, out_file)


def main():
	parser = argparse.ArgumentParser(description='cli-utility for creating ctypes wrappers from C headers')
	
	parser.add_argument(
		'-in', '--in_file', type=str, required=True,
		help=
		"""
		Path to C-header without spaces.
		"""
	)
	
	parser.add_argument(
		'-out', '--out_file', type=str, required=False,
		help=
		"""
		Path to output file. If doesn't exists, will be created.
		"""
	)
	
	parser.add_argument(
		'-co', '--config_folder', type=str, required=False,
		help=
		"""
		Path to configuration folder. Folder must contain folders: TrashWords and Typedefs. These folders must contain use-file 'IN_USE.txt'.
		This file tells which folder files to use for configuration. TrashWords folder should contain files with words to remove. Typedefs 
		folder should contain files with aliases. If not specified, uses basic config folder.
		"""
	)
	
	args = parser.parse_args()
	do_stuff(args)


if __name__ == '__main__':
	main()