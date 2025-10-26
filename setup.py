import os
import sys
from cx_Freeze import setup, Executable


build_exe_options = {
	'packages': [
		'os',
		're',
		'io',
		'sys',
		'argparse'
	],
	'optimize': 2,
	'include_msvcr': True,
}

setup(
	name='ctypes_maker',
	version='0.1',
	description='cli-utility for creating ctypes wrappers',
	options={
		'build_exe': build_exe_options,
	},
	executables=[
		Executable(
			script='main.py',
			base='Console',
			targetName='ctypes_maker.exe',
			icon='lol.ico'
		)
	]
)
