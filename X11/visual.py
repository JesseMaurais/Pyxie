import X11 as X, bit, ctypes

class Info(ctypes.Structure):
	_fields_ = [
		('visual', X.Visual),
		('visualid', X.VisualID),
		('screen', X.INT),
		('depth', X.INT),
		('cclass', X.CARD),
		('red_mask', X.Bitmask),
		('green_mask', X.Bitmask),
		('blue_mask', X.Bitmask),
		('colormap_size', X.INT),
		('bits_per_rgb', X.INT)
		]
		
Mask = bit.mask(
	"""
	None
	ID
	Screen
	Depth
	Class
	RedMask
	GreenMask
	BlueMask
	ColormapSize
	BitsPerRGB
	"""
	)
	
Class = bit.enum(
	"""
	StaticGray
	GrayScale
	StaticColor
	PseudoColor
	TrueColor
	DirectColor
	"""
	)
	
def MaskInfo(**args):
	typemap = {
		'visualid':Mask.ID,
		'screen':Mask.Screen,
		'depth':Mask.Depth,
		'cclass':Mask.Class,
		'red_mask':Mask.RedMask,
		'green_mask':Mask.GreenMask,
		'blue_mask':Mask.BlueMask,
		'colormap_size':Mask.ColormapSize,
		'bits_per_rgb':Mask.BitsPerRGB
		}
	mask = 0
	for key in args:
		mask |= typemap[key]
	return mask, Info(**args)

X.Visual.id = X.extern_property('XVisualIDFromVisual', X.VisualID)
	
X.Display.GetVisualInfo = X.Callable(
	'XGetVisualInfo', X.ArrayOf(Info),
	['self', X.Display],
	['mask', X.Bitmask],
	['template', X.ByRef(Info)],
	['count', X.ByRef(X.INT)]
	)
	
X.Display.MatchVisualInfo = X.Callable(
	'XMatchVisualInfo', X.Status,
	['self', X.Display],
	['screen', X.Integer, 0],
	['depth', X.Integer, 24],
	['cclass', X.Cardinal, Class.DirectColor],
	['return', Info]
	)

