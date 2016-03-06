
__all__ = [
	'GLX',
	'atom',
	'bit',
	'bitmap',
	'colormap',
	'connection',
	'cursor',
	'cutbuffer',
	'defaults',
	'display',
	'drawable',
	'error',
	'event',
	'ext',
	'focus',
	'font',
	'fontquery',
	'fontset',
	'gc',
	'geometry',
	'grab',
	'hint',
	'host',
	'image',
	'io',
	'keyboard',
	'keymap',
	'keysym',
	'kill',
	'pixmap',
	'pointer',
	'region',
	'rm',
	'saveset',
	'screen',
	'screensaver',
	'selection',
	'sync',
	'text',
	'thread',
	'visual',
	'window',
	'wm',
	'xpm',
	'extensions'
	]


### C Language Interface ######################################


import ctypes


INT8 = ctypes.c_int8
INT16 = ctypes.c_int16
INT32 = ctypes.c_int32

CARD8 = ctypes.c_uint8
CARD16 = ctypes.c_uint16
CARD32 = ctypes.c_uint32

STRING8 = ctypes.c_char_p
STRING16 = ctypes.c_wchar_p

BOOL = ctypes.c_int
BYTE = ctypes.c_byte
INT = ctypes.c_int
CARD = ctypes.c_uint


### Types #####################################################


class Bitmask(CARD32):
	pass
class Status(CARD32):
	pass
class Pixel(CARD32):
	pass
class Time(CARD32):
	pass

class KeyCode(CARD8):
	pass
class KeySym(CARD16):
	pass

# Resources

class ID(Bitmask):
	pass
class Atom(ID):
	pass
class Drawable(ID):
	pass
class Window(Drawable):
	pass
class Pixmap(Drawable):
	pass
class Fontable(ID):
	pass
class Font(Fontable):
	pass
class GContext(Fontable):
	pass
class Colormap(ID):
	pass
class VisualID(ID):
	pass
class Cursor(ID):
	pass

# More atomic types

class Integer(INT32):
	pass
class String(STRING8):
	pass
class Cardinal(CARD32):
	pass

# Complex atomic types

class Point(ctypes.Structure):
	_fields_ = [
		('x', INT16),
		('y', INT16)
		]

class Rectangle(ctypes.Structure):
	_fields_ = [
		('x', INT16),
		('y', INT16),
		('width', CARD16),
		('height', CARD16)
		]

class Arc(ctypes.Structure):
	_fields_ = [
		('x', INT16),
		('y', INT16),
		('width', CARD16),
		('height', CARD16),
		('angle1', INT16),
		('angle2', INT16)
		]

# Complex non atomic types

Red = 1 ; Green = 2 ; Blue = 4 ; RGB = Red|Green|Blue

class Color(ctypes.Structure):
	_fields_ = [
		('pixel', Pixel),
		('red', CARD16),
		('green', CARD16),
		('blue', CARD16),
		('flags', CARD8),
		('pad', CARD8)
		]

class Segment(ctypes.Structure):
	_fields_ = [
		('x1', INT16),
		('y1', INT16),
		('x2', INT16),
		('y2', INT16)
		]
		
class PixmapFormat(ctypes.Structure):
	_fields_ = [
		('depth', INT),
		('bits_per_pixel', INT),
		('scanline_pad', INT)
		]

# C objects

class Pointer(ctypes.c_void_p):
	def __init__(self):
		raise RuntimeError('You cannot init opaque C objects')

class Display(Pointer):
	pass
class Screen(Pointer):
	pass
class Visual(Pointer):
	pass
class Keymap(Pointer):
	pass
class GC(Pointer):
	pass
class Image(Pointer):
	pass
class Region(Pointer):
	pass
class FontSet(Pointer):
	pass
class Database(Pointer):
	pass
	
	
### Constants #################################################


CopyFromParent = None

CurrentTime = Time(0)


### Interface #################################################


# Gary Bishop's bag of tricks


class ByRef:
	'Pass argument by reference implicitly'
	
	def __init__(self, ctype):
		self.ctype = ctype
		
	def from_param(self, param):
		if isinstance(param, self.ctype):
			return ctypes.byref(param)

class ListOf:
	'Convert list into array on the fly'
	
	def __init__(self, ctype):
		self.ctype = ctype
		
	def from_param(self, params):
		if isinstance(params, (list, tuple)):
			return (self.ctype * len(params))(*params)


class Wrapper:
	'Define C functions with arity'

	def __init__(self, name):
		from ctypes.util import find_library

		self.lib = ctypes.CDLL(find_library(name))

		if self.lib is None:
			raise RuntimeError('Cannot link Xlib shared object')

	def __call__(self, name, result=int, *args):
		from ctypes import CFUNCTYPE

		types = []
		flags = []
	
		for param in args:
			way = 2 if 'return' in param[0] else 1
		
			if 1 == way:
				types.append(param[1])
			else:
				types.append(ctypes.POINTER(param[1]))
			
			if len(param) > 2:
				flags.append((way, param[0], param[2]))
			else:
				flags.append((way, param[0]))

		call = CFUNCTYPE(result, *types)((name, self.lib), tuple(flags))

		# CFunctionType cannot bind 'self' as the implicit object
		# So we wrap the whole thing in a native function
		# This is not ideal but it works
	
		def thunk(*args, **kwargs):
			return call(*args, **kwargs)
	
		thunk.__name__ = name
		return thunk


# Link the Xlib shared object


Callable = Wrapper('X11')


# My own bag of tricks


def extern_property(name, type=None, lib=Callable.lib):
	'Treat a unary C function as a class property of a C object'
	
	address = lib[name]

	if type is None:
		return property(address)
	else:
		address.restype = type

	def thunk_by_value(self):
		return address(self).value
		
	def thunk(self):
		return address(self)
	
	if issubclass(type, (ctypes.c_char_p, ctypes.c_bool)):
		return property(thunk_by_value)
	else:
		return property(thunk)


def CurrentDisplayAttribute(self, name):
	'Use a display reference to forward a resource class method'
	
	attr = getattr(Display.current, name)
	if callable(attr):
		return lambda *args, **kwargs: attr(self, *args, **kwargs)


ID.__getattr__ = CurrentDisplayAttribute
GC.__getattr__ = CurrentDisplayAttribute
Visual.__getattr__ = CurrentDisplayAttribute
FontSet.__getattr__ = CurrentDisplayAttribute


### Core Display Methods ######################################


OpenDisplay = Callable(
	'XOpenDisplay', Display,
	['name', String, None]
	)

Display.Close = Callable(
	'XCloseDisplay', int,
	['self', Display]
	)

Display.Flush = Callable(
	'XFlush', int,
	['self', Display]
	)


# Sugar (see CurrentDisplayAttribute)


def MakeCurrent(display=None):
	'Set a class attribute representing the current display'
	assert isinstance(display, Display)
	if display is not None:
		setattr(Display, 'current', display)
	else:
		delattr(Display, 'current')	

def Open(display_name=None):
	'Auto-set the current display when opened'
	display = OpenDisplay(display_name)
	MakeCurrent(display)
	return display


#### Client Memory ############################################


Free = Callable.lib.XFree
FreeStringList = Callable.lib.XFreeStringList
FreeExtensionList = Callable.lib.XFreeExtensionList
FreeFontPath = Callable.lib.XFreeFontPath
FreeFontNames = Callable.lib.XFreeFontNames

def AddressOf(ctype):
	return ctypes.POINTER(ctype)

def ArrayOf(ctype):
	return AddressOf(ctype)

