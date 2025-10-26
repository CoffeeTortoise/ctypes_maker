import sys


PLATFORM = sys.platform

CODING = 'utf-8'

ENDL = '\_(-_-)_/'

REPLACER = 'LOL'

USE_FILENAME = 'IN_USE.txt'

NUMS = tuple(str(i) for i in xrange(10))

COMMENTS = '*', '//', '/*', '*/', '\\'

MACROSES = '#include', '#ifdef', '#endif', '#if', '#elif', '#ifndef', '#undef', '#else', 'defined', '#error', '#pragma'

USELESS_STUFF = (
	'__asm__', 'if(', 'return', '//', 'if', 'switch', 'else',
	':', '@', '!', '$', '%', '^', '+', '-', '/', '=', '~', '.',
	'extern \"C\"', '?', '<', '>', '|', '-'
)

WINTYPES_TABLE = {
	"BYTE": "ctypes.wintypes.BYTE",
	"WORD": "ctypes.wintypes.WORD",
	"SHORT": "ctypes.wintypes.SHORT",
	"INT": "ctypes.wintypes.INT",
	"UINT": "ctypes.wintypes.UINT",
	"LONG": "ctypes.wintypes.LONG",
	"ULONG": "ctypes.wintypes.ULONG",
	"DWORD": "ctypes.wintypes.DWORD",
	"DWORDLONG": "ctypes.wintypes.DWORDLONG",
	"INT_PTR": "ctypes.wintypes.INT_PTR",
	"UINT_PTR": "ctypes.wintypes.UINT_PTR",
	"LONG_PTR": "ctypes.wintypes.LONG_PTR",
	"ULONG_PTR": "ctypes.wintypes.ULONG_PTR",
	"BOOL": "ctypes.wintypes.BOOL",
	"BOOLEAN": "ctypes.wintypes.BOOLEAN",
	"LPSTR": "ctypes.wintypes.LPSTR",
	"LPCSTR": "ctypes.wintypes.LPCSTR",
	"LPWSTR": "ctypes.wintypes.LPWSTR",
	"LPCWSTR": "ctypes.wintypes.LPCWSTR",
	"LPVOID": "ctypes.wintypes.LPVOID",
	"PVOID": "ctypes.wintypes.PVOID",
	"SIZE_T": "ctypes.wintypes.SIZE_T",
	"SSIZE_T": "ctypes.wintypes.SSIZE_T",
	"HANDLE": "ctypes.wintypes.HANDLE",
	"HKEY": "ctypes.wintypes.HKEY",
	"HINSTANCE": "ctypes.wintypes.HINSTANCE",
	"HMODULE": "ctypes.wintypes.HMODULE",
	"HWND": "ctypes.wintypes.HWND",
	"COLORREF": "ctypes.wintypes.COLORREF",
	"POINT": "ctypes.wintypes.POINT",
	"POINTL": "ctypes.wintypes.POINTL",
	"RECT": "ctypes.wintypes.RECT",
	"RECTL": "ctypes.wintypes.RECTL",
	"MSG": "ctypes.wintypes.MSG",
	"FILETIME": "ctypes.wintypes.FILETIME",
	"SYSTEMTIME": "ctypes.wintypes.SYSTEMTIME",
	"SECURITY_ATTRIBUTES": "ctypes.wintypes.SECURITY_ATTRIBUTES",
	"OVERLAPPED": "ctypes.wintypes.OVERLAPPED",
	"EXCEPTION_POINTERS": "ctypes.wintypes.EXCEPTION_POINTERS",
	"PIXELFORMATDESCRIPTOR": "ctypes.wintypes.PIXELFORMATDESCRIPTOR",
}

TYPES_TABLE = {
	'...': '',
	'HRESULT': 'ctypes.HRESULT',
	'PyObject': 'ctypes.py_object',
	'_Bool': 'ctypes.c_bool', 
	'void': 'None', 
	'char': 'ctypes.c_char',
	'wchar_t': 'ctypes.c_wchar', 
	'byte': 'ctypes.c_byte', 
	'unsigned char': 'ctypes.c_ubyte',
	'short': 'ctypes.c_short', 
	'unsigned short': 'ctypes.c_ushort', 
	'int': 'ctypes.c_int',
	'unsigned int': 'ctypes.c_uint', 
	'long': 'ctypes.c_long', 
	'unsigned long': 'ctypes.c_ulong',
	'__int8': 'ctypes.c_int8',
	'__int16': 'ctypes.c_int16',
	'__int32': 'ctypes.c_int32',
	'__int64': 'ctypes.c_longlong', 
	'long long': 'ctypes.c_longlong', 
	'unsigned __int8': 'ctypes.c_uint8',
	'unsigned __int16': 'ctypes.c_uint16',
	'unsigned __int32': 'ctypes.c_uint32',
	'unsigned __int64': 'ctypes.c_ulonglong',
	'unsigned long long': 'ctypes.c_ulonglong', 
	'size_t': 'ctypes.c_size_t', 
	'ssize_t': 'ctypes.c_ssize_t',
	'Py_ssize_t': 'ctypes.c_ssize_t', 
	'float': 'ctypes.c_float', 
	'double': 'ctypes.c_double',
	'long double': 'ctypes.c_longdouble', 
	'char*': 'ctypes.c_char_p', 
	'wchar_t*': 'ctypes.c_wchar_p', 
	'void*': 'ctypes.c_void_p', 
}

if PLATFORM == 'win32':
	TYPES_TABLE.update(WINTYPES_TABLE)
