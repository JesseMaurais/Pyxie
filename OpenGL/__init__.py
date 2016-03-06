__all__ = ['utility']

import ctypes, sys
from ctypes.util import find_library

lib = ctypes.CDLL(find_library('GL'))

GLbyte = ctypes.c_byte
GLshort = ctypes.c_short
GLint = ctypes.c_long

GLubyte = ctypes.c_ubyte
GLushort = ctypes.c_ushort
GLuint = ctypes.c_ulong

GLfloat = ctypes.c_float
GLdouble = ctypes.c_double

GLenum = GLuint
GLboolean = GLubyte
GLbitfield = GLuint
GLsizei = GLint
GLclampf = GLfloat
GLclampd = GLdouble
GLvoid = None
void = None


class ExtensionError(RuntimeError):
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return 'Symbol %s is not in OpenGL' % self.name


def extend(ext):

	index = ext.find('_')
	def mangle(name):
		from string import digits
		if name[index] == '_':
			if name[index+1] not in digits:
				return name[index+1:]
		return name[index:]

	def typemap(name):
		if 'const' in name:
			name = name.split()[1]

		if 'GLvoid*' == name:
			return ctypes.c_void_p
		if 'GLubyte*' == name:
			return ctypes.c_char_p
		if 'char*' == name:
			return ctypes.c_char_p

		ptr = name.count('*')
		name = name.strip('*')
		typename = eval(name)

		if ptr:
			return ctypes.POINTER(typename)
		else:
			return typename

	def token(elem):
		attr = elem.attrib
		name = attr['name']
		value = attr['value']
		return mangle(name), eval(value)

	def params(elem):
		for item in elem:
			attr = item.attrib
			kind = attr['type']
			yield typemap(kind)

	def function(elem):
		attr = elem.attrib
		name = attr['name']

		if not hasattr(lib, name):
			raise ExtensionError(name)

		link = lib[name]
		link.restype = typemap(attr['return'])
		for item in elem:
			if item.tag == 'params':
				link.argtypes = [arg for arg in params(item)]

		return mangle(name), link
		
	def parse(elem):
		for item in elem:
			if item.tag == 'token':
				yield token(item)
			if item.tag == 'function':
				yield function(item)

	from lxml import etree
	import os

	path = os.path.abspath(__file__)
	dir = os.path.split(path)[0]

	doc = etree.parse(dir + '/' + ext + '.xml')
	root = doc.getroot()

	attr = root.attrib
	if 'depend' in attr:
		require(attr['depend'])

	for elem in root:
		for name, item in parse(elem):
			sys.modules[__name__].__dict__[name] = item

def require(ext):
	for e in ext.split():
		extend(e)

