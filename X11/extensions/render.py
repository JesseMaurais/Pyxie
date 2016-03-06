import X11 as X, ctypes
from X11 import bit

Callable = X.Wrapper('Xrender')

X.Display.QueryRenderExtension = Callable(
	'XRenderQueryExtension', bool,
	['self', X.Display],
	['event_return', X.CARD],
	['error_return', X.CARD]
	)

X.Display.QueryRenderVersion = Callable(
	'XRenderQueryVersion', X.Status,
	['self', X.Display],
	['major_version_return', X.INT],
	['minor_version_return', X.INT]
	)

# Resources

class Glyph(X.ID):
	pass
class GlyphSet(X.ID):
	pass
class Picture(X.ID):
	pass
class PictureFormat(X.ID):
	pass
class PictureOperation(X.ID):
	pass

# Constants

PictOp = bit.enum(
	"""
	Clear
	Src
	Dst
	Over
	OverReverse
	In
	InReverse
	Out
	OutReverse
	Atop
	AtopReverse
	Xor
	Add
	Saturate
	.
	.
	DisjointClear
	DisjointSrc
	DisjointDst
	DisjointOver
	DisjointOverReverse
	DisjointIn
	DisjointInReverse
	DisjointOut
	DisjointOutReverse
	DisjointAtop
	DisjointAtopReverse
	DisjointAtopXor
	.
	.
	.
	.
	ConjointClear
	ConjointSrc
	ConjointDst
	ConjointOver
	ConjointOverReverse
	ConjointIn
	ConjointInReverse
	ConjointOut
	ConjointOutReverse
	ConjointAtop
	ConjointAtopReverse
	ConjointXor
	.
	.
	.
	.
	Multiply
	Screen
	Overlay
	Darken
	Lighten
	ColorDodge
	ColorBurn
	HardLight
	SoftLight
	Difference
	Exclusion
	HSLHue
	HSLSaturation
	HSLColor
	HSLLuminosity
	"""
	,t=PictureOperation
	)


### Shapes ####################################################


class Fixed(X.CARD):
	@property
	def real(self):
		return float(self.value) / 65535
	def __init__(self, real):
		self.value = int(real * 65535)

class Point(ctypes.Structure):
	_fields_ = [
		('x', Fixed),
		('y', Fixed)
		]

class Line(ctypes.Structure):
	_fields_ = [
		('p1', Point),
		('p2', Point)
		]

class Triangle(ctypes.Structure):
	_fields_ = [
		('p1', Point),
		('p2', Point),
		('p3', Point)
		]
		
class Circle(ctypes.Structure):
	_fields_ = [
		('center', Point),
		('radius', Fixed)
		]

class Trapezoid(ctypes.Structure):
	_fields_ = [
		('top', Fixed),
		('bottom', Fixed),
		('left', Line),
		('right', Line)
		]

# Algebra

class Vector(ctypes.Structure):
	_fields_ = [
		('x', Fixed),
		('y', Fixed),
		('z', Fixed)
		]
		
class Matrix(ctypes.Structure):
	_fields_ = [
		('v1', Vector),
		('v2', Vector),
		('v3', Vector)
		]

# More Trapezoids

class Span(ctypes.Structure):
	_fields_ = [
		('left', Fixed),
		('right', Fixed),
		('y', Fixed)
		]

class Trap(ctypes.Structure):
	_fields_ = [
		('top', Span),
		('bottom', Span)
		]

# Color

class Color(ctypes.Structure):
	_fields_ = [
		('red', X.CARD16),
		('green', X.CARD16),
		('blue', X.CARD16),
		('alpha', X.CARD16)
		]
		
	def __init__(self, R=1.0, G=1.0, B=1.0, A=1.0):
		self.red = int(R*0xffff)
		self.green = int(G*0xffff)
		self.blue = int(B*0xffff)
		self.alpha = int(A*0xffff)

X.Display.RenderColor = Callable(
	'XRenderParseColor', X.Status,
	['self', X.Display],
	['spec', X.String],
	['return', Color]
	)


### Pixel #####################################################


Subpixel = bit.enum(
	"""
	Unknown
	HorizontalRGB
	HorizontalBGR
	VerticalRGB
	VerticalBGR
	None
	"""
	)

X.Display.QuerySubpixelOrder = Callable(
	'XRenderQuerySubpixelOrder', int,
	['self', X.Display],
	['screen', X.Integer, 0]
	)

X.Display.SetSubpixelOrder = Callable(
	'XRenderSetSubpixelOrder', bool,
	['self', X.Display],
	['screen', X.Integer, 0],
	['subpixel', X.Cardinal, Subpixel.HorizontalRGB]
	)


### Filter ####################################################


class Filters(ctypes.Structure):
	_fields_ = [
		('nfilter', X.INT),
		('filter', X.ArrayOf(X.STRING8)),
		('nalias', X.INT),
		('alias', X.ArrayOf(X.STRING8))
		]

X.Display.QueryFilters = Callable(
	'XRenderQueryFilters', X.AddressOf(Filters),
	['self', X.Display],
	['drawable', X.Drawable]
	)

X.Display.SetPictureFilter = Callable(
	'XRenderSetPictureFilter', None,
	['self', X.Display],
	['picture', Picture],
	['filter', X.String],
	['params', X.ListOf(Fixed)],
	['nparams', X.Integer]
	)


### Format ####################################################


X.Display.QueryFormats = Callable(
	'XRenderQueryFormats', X.Status,
	['self', X.Display]
	)

class Format(ctypes.Structure):
	_fields_ = [
		('id', PictureFormat),
		('type', X.INT),
		('depth', X.INT),
		('red', X.INT16),
		('red_mask', X.INT16),
		('green', X.INT16),
		('green_mask', X.INT16),
		('blue', X.INT16),
		('blue_mask', X.INT16),
		('alpha', X.INT16),
		('alpha_mask', X.INT16),
		('colormap', X.Colormap)
		]

FormatMask = bit.mask(
	"""
	ID
	Type
	Depth
	Red
	RedMask
	Green
	GreenMask
	Blue
	BlueMask
	Alpha
	AlphaMask
	Colormap
	"""
	)

PictureType = bit.enum(
	"""
	Indexed
	Direct
	"""
	)

Standard = bit.enum(
	"""
	ARGB32
	RGB24
	A8
	A4
	A1
	"""
	)

X.Display.FindVisualFormat = Callable(
	'XRenderFindVisualFormat', X.AddressOf(Format),
	['self', X.Display],
	['visual', X.Visual]
	)

X.Visual.format = property(lambda visual: visual.FindVisualFormat())

X.Display.FindFormat = Callable(
	'XRenderFindFormat', X.AddressOf(Format),
	['self', X.Display],
	['mask', X.Bitmask],
	['template', X.ByRef(Format)],
	['count', X.ByRef(X.INT)]
	)

X.Display.FindStandardFormat = Callable(
	'XRenderFindStandardFormat', X.AddressOf(Format),
	['self', X.Display],
	['format', X.CARD, Standard.ARGB32]
	)

class IndexValue(ctypes.Structure):
	_fields_ = [
		('pixel', X.Pixel),
		('red', X.CARD16),
		('green', X.CARD16),
		('blue', X.CARD16)
		]

X.Display.QueryPictIndexValues = Callable(
	'XRenderQueryPictIndexValues', X.AddressOf(IndexValue),
	['self', X.Display],
	['format', X.ByRef(Format)],
	['count', X.ByRef(X.INT)]
	)


### Gradient ##################################################


X.Display.CreateSolidFill = Callable(
	'XRenderCreateSolidFill', Picture,
	['self', X.Display],
	['color', X.ByRef(Color)]
	)

class LinearGradient(ctypes.Structure):
	_fields_ = [
		('p1', Point),
		('p2', Point)
		]

X.Display.CreateLinearGradient = Callable(
	'XRenderCreateLinearGradient', Picture,
	['self', X.Display],
	['gradient', X.ByRef(LinearGradient)],
	['stops', X.ListOf(Fixed)],
	['colors', X.ListOf(Color)],
	['nstops', X.Integer]
	)

class RadialGradient(ctypes.Structure):
	_fields_ = [
		('inner', Circle),
		('outer', Circle)
		]

X.Display.CreateRadialGradient = Callable(
	'XRenderCreateRadialGradient', Picture,
	['self', X.Display],
	['gradient', X.ByRef(RadialGradient)],
	['stops', X.ListOf(Fixed)],
	['colors', X.ListOf(Color)],
	['nstops', X.Integer]
	)

class ConicalGradient(ctypes.Structure):
	_fields_ = [
		('center', Point),
		('angle', Fixed)
		]

X.Display.CreateConicalGradient = Callable(
	'XRenderCreateConicalGradient', Picture,
	['self', X.Display],
	['gradient', X.ByRef(ConicalGradient)],
	['stops', X.ListOf(Fixed)],
	['colors', X.ListOf(Color)],
	['nstops', X.Integer]
	)


### Picture ###################################################


class Attributes(ctypes.Structure):
	_fields_ = [
		('repeat', X.CARD),
		('alpha_map', Picture),
		('alpha_x_origin', X.INT),
		('alpha_y_origin', X.INT),
		('clip_x_origin', X.INT),
		('clip_y_origin', X.INT),
		('clip_mask', X.Pixmap),
		('graphics_exposures', X.BOOL),
		('subwindow_mode', X.CARD),
		('poly_edge', X.CARD),
		('poly_mode', X.CARD),
		('dither', X.BOOL),
		('component_alpha', X.BOOL)
		]

Mask = bit.mask(
	"""
	Repeat
	AlphaMap
	AlphaXOrigin
	AlphaYOrigin
	ClipXOrigin
	ClipYOrigin
	ClipMask
	GraphicsExposure
	SubwindowMode
	PolyEdge
	PolyMode
	Dither
	ComponentAlpha
	"""
	)
	
def MaskAttributes(**args):
	typemap = {
		'repeat':Mask.Repeat,
		'alpha_map':Mask.AlphaMap,
		'alpha_x_origin':Mask.AlphaXOrigin,
		'alpha_y_origin':Mask.AlphaYOrigin,
		'clip_x_origin':Mask.ClipXOrigin,
		'clip_y_origin':Mask.ClipYOrigin,
		'clip_mask':Mask.ClipMask,
		'graphics_exposures':Mask.GraphicsExposure,
		'subwindow_mode':Mask.SubwindowMode,
		'poly_edge':Mask.PolyEdge,
		'poly_mode':Mask.PolyMode,
		'dither':Mask.Dither,
		'component_alpha':Mask.ComponentAlpha
		}
	mask = 0
	for key in args:
		mask |= typemap[key]
	return mask, Attributes(**args)

Repeat = bit.enum(
	"""
	None
	Normal
	Pad
	Reflect
	"""
	)

PolyEdge = bit.enum(
	"""
	Sharp
	Smooth
	"""
	)

PolyMode = bit.enum(
	"""
	Precise
	Imprecise
	"""
	)

X.Display.CreatePicture = Callable(
	'XRenderCreatePicture', Picture,
	['self', X.Display],
	['drawable', X.Drawable],
	['format', X.AddressOf(Format)],
	['mask', X.Bitmask, 0],
	['attributes', X.AddressOf(Attributes), None]
	)
	
X.Display.FreePicture = Callable(
	'XRenderFreePicture', None,
	['self', X.Display],
	['picture', Picture]
	)
	
X.Display.ChangePicture = Callable(
	'XRenderChangePicture', None,
	['self', X.Display],
	['picture', Picture],
	['mask', X.Bitmask],
	['attributes', X.ByRef(Attributes)]
	)
	
X.Display.SetPictureClipRectangles = Callable(
	'XRenderSetPictureClipRectangles', None,
	['self', X.Display],
	['picture', Picture],
	['xorigin', X.Integer],
	['yorigin', X.Integer],
	['rects', X.ArrayOf(X.Rectangle)],
	['nrects', X.INT]
	)

X.Display.SetPictureClipRegion = Callable(
	'XRenderSetPictureClipRegion', None,
	['self', X.Display],
	['picture', Picture],
	['region', X.Region]
	)

X.Display.SetPictureTransform = Callable(
	'XRenderSetPictureTransform', None,
	['self', X.Display],
	['picture', Picture],
	['transform', Matrix]
	)

X.Display.AddTraps = Callable(
	'XRenderAddTraps', None,
	['self', X.Display],
	['picture', Picture],
	['xoffset', X.Integer],
	['yoffset', X.Integer],
	['traps', X.ListOf(Trap)],
	['ntraps', X.Integer]
	)

X.Display.Composite = Callable(
	'XRenderComposite', None,
	['self', X.Display],
	['op', PictureOperation],
	['src', Picture],
	['mask', Picture],
	['dst', Picture],
	['src_x', X.Integer, 0],
	['src_y', X.Integer, 0],
	['mask_x', X.Integer, 0],
	['mask_y', X.Integer, 0],
	['dst_x', X.Integer, 0],
	['dst_y', X.Integer, 0],
	['width', X.Integer],
	['height', X.Integer]
	)


### Cursor ####################################################


class AnimCursor(ctypes.Structure):
	_fields_ = [
		('cursor', X.Cursor),
		('delay', X.Time)
		]

X.Display.CreateAnimCursor = Callable(
	'XRenderCreateAnimCursor', X.Cursor,
	['self', X.Display],
	['ncursors', X.Integer],
	['cursor', X.ListOf(AnimCursor)]
	)

X.Display.CreateCursor = Callable(
	'XRenderCreateCursor', X.Cursor,
	['self', X.Display],
	['picture', Picture],
	['x', X.Integer],
	['y', X.Integer]
	)


### Glyph #####################################################


class GlyphInfo(ctypes.Structure):
	_fields_ = [
		('width', X.INT16),
		('height', X.INT16),
		('x', X.INT16),
		('y', X.INT16),
		('xoff', X.INT16),
		('yoff', X.INT16)
		]

X.Display.CreateGlyphSet = Callable(
	'XRenderCreateGlyphSet', GlyphSet,
	['self', X.Display],
	['format', X.ByRef(Format)]
	)
	
X.Display.ReferenceGlyphSet = Callable(
	'XRenderReferenceGlyphSet', GlyphSet,
	['self', X.Display],
	['existing', GlyphSet]
	)
	
X.Display.FreeGlyphSet = Callable(
	'XRenderFreeGlyphSet', None,
	['self', X.Display],
	['glyphset', GlyphSet]
	)
	
X.Display.AddGlyphs = Callable(
	'XRenderAddGlyphs', None,
	['self', X.Display],
	['glyphset', GlyphSet],
	['glyphs', X.ArrayOf(Glyph)],
	['infos', X.ArrayOf(GlyphInfo)],
	['nglyphs', X.Integer],
	['images', X.String],
	['nimages', X.Integer]
	)
	
X.Display.FreeGlyphs = Callable(
	'XRenderFreeGlyphs', None,
	['self', X.Display],
	['glyphset', GlyphSet],
	['glyphs', X.ArrayOf(Glyph)],
	['nglyphs', X.Integer]
	)


### Shapes ####################################################


X.Display.CompositeFillRectangle = Callable(
	'XRenderFillRectangle', None,
	['self', X.Display],
	['op', PictureOperation],
	['dst', Picture],
	['color', X.ByRef(Color)],
	['x', X.Integer, 0],
	['y', X.Integer, 0],
	['width', X.Integer, 1],
	['height', X.Integer, 1]
	)

X.Display.CompositeFillRectangles = Callable(
	'XRenderFillRectangles', None,
	['self', X.Display],
	['op', PictureOperation],
	['dst', Picture],
	['color', X.ByRef(Color)],
	['rects', X.ListOf(X.Rectangle)],
	['nrects', X.Integer]
	)

X.Display.CompositeTrapezoids = Callable(
	'XRenderCompositeTrapezoids', None,
	['self', X.Display],
	['op', PictureOperation],
	['src', Picture],
	['dst', Picture],
	['mask', X.ByRef(Format)],
	['src_x', X.Integer],
	['src_y', X.Integer],
	['traps', X.ListOf(Trapezoid)],
	['ntraps', X.Integer]
	)

X.Display.CompositeTriangles = Callable(
	'XRenderCompositeTriangles', None,
	['self', X.Display],
	['op', PictureOperation],
	['src', Picture],
	['dst', Picture],
	['mask', X.ByRef(Format)],
	['src_x', X.Integer],
	['src_y', X.Integer],
	['tris', X.ListOf(Triangle)],
	['ntris', X.Integer]
	)

X.Display.CompositeTriStrip = Callable(
	'XRenderCompositeTriStrip', None,
	['self', X.Display],
	['op', PictureOperation],
	['src', Picture],
	['dst', Picture],
	['mask', X.ByRef(Format)],
	['src_x', X.Integer],
	['src_y', X.Integer],
	['points', X.ListOf(Point)],
	['npoints', X.Integer]
	)

X.Display.CompositeTriFan = Callable(
	'XRenderCompositeTriFan', None,
	['self', X.Display],
	['op', PictureOperation],
	['src', Picture],
	['dst', Picture],
	['mask', X.ByRef(Format)],
	['src_x', X.Integer],
	['src_y', X.Integer],
	['points', X.ListOf(Point)],
	['npoints', X.Integer]
	)

### String ####################################################


X.Display.CompositeString8 = Callable(
	'XRenderCompositeString8', None,
	['self', X.Display],
	['op', PictureOperation],
	['src', Picture],
	['dst', Picture],
	['mask', X.ByRef(Format)],
	['glyphset', GlyphSet],
	['src_x', X.Integer],
	['src_y', X.Integer],
	['dst_x', X.Integer],
	['dst_y', X.Integer],
	['string', X.STRING8],
	['strlen', X.Integer]
	)

X.Display.CompositeString16 = Callable(
	'XRenderCompositeString16', None,
	['self', X.Display],
	['op', PictureOperation],
	['src', Picture],
	['dst', Picture],
	['mask', X.ByRef(Format)],
	['glyphset', GlyphSet],
	['src_x', X.Integer],
	['src_y', X.Integer],
	['dst_x', X.Integer],
	['dst_y', X.Integer],
	['string', X.STRING16],
	['strlen', X.Integer]
	)

# XRenderCompositeString32


### Text ######################################################


class GlyphElt8(ctypes.Structure):
	_fields_ = [
		('glyphset', GlyphSet),
		('chars', X.STRING8),
		('nchars', X.INT),
		('xoffset', X.INT),
		('yoffset', X.INT)
		]

X.Display.CompositeText8 = Callable(
	'XRenderCompositeText8', None,
	['self', X.Display],
	['op', PictureOperation],
	['src', Picture],
	['dst', Picture],
	['mask', X.ByRef(Format)],
	['src_x', X.Integer],
	['src_y', X.Integer],
	['dst_x', X.Integer],
	['dst_y', X.Integer],
	['elts', X.ListOf(GlyphElt8)],
	['nelts', X.Integer]
	)

class GlyphElt16(ctypes.Structure):
	_fields_ = [
		('glyphset', GlyphSet),
		('chars', X.STRING16),
		('nchars', X.INT),
		('xoffset', X.INT),
		('yoffset', X.INT)
		]

X.Display.CompositeText16 = Callable(
	'XRenderCompositeText16', None,
	['self', X.Display],
	['op', PictureOperation],
	['src', Picture],
	['dst', Picture],
	['mask', X.ByRef(Format)],
	['src_x', X.Integer],
	['src_y', X.Integer],
	['dst_x', X.Integer],
	['dst_y', X.Integer],
	['elts', X.ListOf(GlyphElt16)],
	['nelts', X.Integer]
	)

# XRenderCompositeText32

