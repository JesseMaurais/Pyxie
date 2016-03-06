import OpenGL as GL
import X11 as X


class Context(X.Pointer):
	pass
class FBConfig(X.Pointer):
	pass
class Pbuffer(X.ID):
	pass
class XVisualInfo(X.Pointer):
	pass


void = None
Display = X.Display
XID = X.ID
Pixmap = X.Pixmap
Font = X.Font

GLXDrawable = X.Drawable
GLXPixmap = X.Pixmap
GLXWindow = X.Window
GLXContext = Context
GLXPbuffer = Pbuffer
GLXFBConfig = FBConfig

GLint = X.Integer
GLuint = X.Cardinal
Bool = X.BOOL


def extend(ext):

	index = ext.find('_')
	def mangle(name):
		from string import digits
		if name[index] == '_':
			if name[index+1] not in digits:
				return name[index+1:]
		return name[index:]

	def typemap(name):
		from ctypes import POINTER

		if 'const' in name:
			name = name.split()[1]

		if 'GLubyte*' == name:
			return String

		ptr = name.count('*')
		name = name.strip('*')
		typename = eval(name)

		if ptr:
			return POINTER(typename)
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

		if not hasattr(GL.lib, name):
			raise GL.ExtensionError(name)

		link = GL.lib[name]
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
	import os, sys

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

