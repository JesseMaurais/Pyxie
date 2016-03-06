import X11 as X, bit, ctypes

class Values(ctypes.Structure):
	_fields_ = [
		('function', X.CARD),
		('plane_mask', X.Bitmask),
		('foreground', X.Pixel),
		('background', X.Pixel),
		('line_width', X.INT),
		('line_style', X.CARD),
		('cap_style', X.CARD),
		('join_style', X.CARD),
		('fill_style', X.CARD),
		('fill_rule', X.CARD),
		('arc_mode', X.CARD),
		('tile', X.Pixmap),
		('stipple', X.Pixmap),
		('ts_x_origin', X.INT),
		('ts_y_origin', X.INT),
		('font', X.Font),
		('subwindow_mode', X.CARD),
		('graphics_exposures', X.BOOL),
		('clip_x_origin', X.INT),
		('clip_y_origin', X.INT),
		('clip_mask', X.Pixmap),
		('dash_offset', X.INT),
		('dashes', X.BYTE)
		]

Mask = bit.mask(
	"""
	Function
	PlaneMask
	Foreground
	Background
	LineWidth
	LineStyle
	CapStyle
	JoinStyle
	FillStyle
	Tile
	Stipple
	TileStipXOrigin
	TileStipYOrigin
	Font
	SubwindowMode
	GraphicsExposures
	ClipXOrigin
	ClipYOrigin
	ClipMask
	DashOffset
	DashList
	ArcMode
	"""
	)

def MaskValues(**args):
	typemap = {
		'function':Mask.Function,
		'plane_mask':Mask.PlaneMask,
		'foreground':Mask.Foreground,
		'background':Mask.Background,
		'line_width':Mask.LineWidth,
		'line_style':Mask.LineStyle,
		'cap_style':Mask.CapStyle,
		'join_style':Mask.JoinStyle,
		'fill_style':Mask.FillStyle,
		'arc_mode':Mask.ArcMode,
		'tile':Mask.Tile,
		'stipple':Mask.Stipple,
		'ts_x_origin':Mask.TileStipXOrigin,
		'ts_y_origin':Mask.TileStipYOrigin,
		'font':Mask.Font,
		'subwindow_mode':Mask.SubwindowMode,
		'graphics_exposures':Mask.GraphicsExposures,
		'clip_x_origin':Mask.ClipXOrigin,
		'clip_y_origin':Mask.ClipYOrigin,
		'clip_mask':Mask.ClipMask,
		'dash_offset':Mask.DashOffset,
		'dashes':Mask.DashList
		}
	mask = 0
	for key in args:
		mask |= typemap[key]
	return mask, Values(**args)


### Constants #################################################


GX = bit.enum(
	"""
	Clear
	And
	AndReverse
	Copy
	AndInverted
	NoOp
	Xor
	Or
	Nor
	Equiv
	Invert
	OrReverse
	CopyInverted
	OrInverted
	Nand
	Set
	"""
	)

Line = bit.enum(
	"""
	Solid
	OnOffDash
	DoubleDash
	"""
	)

Cap = bit.enum(
	"""
	NotLast
	Butt
	Round
	Projecting
	"""
	)

Join = bit.enum(
	"""
	Miter
	Round
	Bevel
	"""
	)

Fill = bit.enum(
	"""
	Solid
	Tiled
	Stippled
	OpaqueStippled
	"""
	)

FillRule = bit.enum(
	"""
	EvenOdd
	Winding
	"""
	)

SubwindowMode = bit.enum(
	"""
	ClipByChildren
	IncludeInferiors
	"""
	)


### Methods ###################################################


X.GC.id = X.extern_property('XGContextFromGC', X.GContext)

X.Display.CreateGC = X.Callable(
	'XCreateGC', X.GC,
	['self', X.Display],
	['drawable', X.Drawable],
	['mask', X.Bitmask, 0],
	['values', X.AddressOf(Values), None]
	)
	
X.Display.FreeGC = X.Callable(
	'XFreeGC', int,
	['self', X.Display],
	['gc', X.GC]
	)
	
X.Display.CopyGC = X.Callable(
	'XCopyGC', int,
	['self', X.Display],
	['src', X.GC],
	['dst', X.GC],
	['mask', X.Bitmask, Mask.every]
	)
	
X.Display.ChangeGC = X.Callable(
	'XChangeGC', int,
	['self', X.Display],
	['gc', X.GC],
	['mask', X.Bitmask],
	['values', X.ByRef(Values)]
	)
	
X.Display.GetGCValues = X.Callable(
	'XGetGCValues', X.Status,
	['self', X.Display],
	['gc', X.GC],
	['mask', X.Bitmask, Mask.every],
	['return_values', Values]
	)


### Query Best Sizes ##########################################

	
X.Display.QueryBestTile = X.Callable(
	'XQueryBestTile', X.Status,
	['self', X.Display],
	['drawable', X.Drawable],
	['width', X.Integer],
	['height', X.Integer],
	['return_width', X.INT],
	['return_height', X.INT]
	)
	
X.Display.QueryBestStipple = X.Callable(
	'XQueryBestStipple', X.Status,
	['self', X.Display],
	['drawable', X.Drawable],
	['width', X.Integer],
	['height', X.Integer],
	['return_width', X.INT],
	['return_height', X.INT]
	)
	
	
### Set GC Values #############################################


X.Display.FlushGC = X.Callable(
	'XFlushGC', None,
	['self', X.Display],
	['gc', X.GC]
	)
	
X.Display.SetState = X.Callable(
	'XSetState', int,
	['self', X.Display],
	['gc', X.GC],
	['foreground', X.Pixel],
	['background', X.Pixel],
	['function', X.Cardinal],
	['plane_mask', X.Bitmask]
	)
	
X.Display.SetLineAttributes = X.Callable(
	'XSetLineAttributes', int,
	['self', X.Display],
	['gc', X.GC],
	['line_width', X.Integer],
	['line_style', X.Cardinal],
	['cap_style', X.Cardinal],
	['join_style', X.Cardinal]
	)
	
X.Display.SetFillRule = X.Callable(
	'XSetFillRule', int,
	['self', X.Display],
	['gc', X.GC],
	['rule', X.Cardinal]
	)
	
X.Display.SetFillStyle = X.Callable(
	'XSetFillStyle', int,
	['self', X.Display],
	['gc', X.GC],
	['style', X.Cardinal]
	)
	
X.Display.SetDashes = X.Callable(
	'XSetDashes', int,
	['self', X.Display],
	['gc', X.GC],
	['offset', X.Integer],
	['dashes', X.ListOf(X.BYTE)],
	['n_dashes', X.Integer]
	)
	
X.Display.SetForeground = X.Callable(
	'XSetForeground', int,
	['self', X.Display],
	['gc', X.GC],
	['foreground', X.Pixel]
	)
	
X.Display.SetBackground = X.Callable(
	'XSetBackground', int,
	['self', X.Display],
	['gc', X.GC],
	['background', X.Pixel]
	)
	
X.Display.SetFunction = X.Callable(
	'XSetFunction', int,
	['self', X.Display],
	['gc', X.GC],
	['function', X.Cardinal]
	)
	
X.Display.SetPlaneMask = X.Callable(
	'XSetPlaneMask', int,
	['self', X.Display],
	['gc', X.GC],
	['mask', X.Bitmask]
	)
	
X.Display.SetArcMode = X.Callable(
	'XSetArcMode', int,
	['self', X.Display],
	['gc', X.GC],
	['mode', X.Cardinal]
	)
	
X.Display.SetTile = X.Callable(
	'XSetTile', int,
	['self', X.Display],
	['gc', X.GC],
	['tile', X.Pixmap]
	)
	
X.Display.SetStipple = X.Callable(
	'XSetStipple', int,
	['self', X.Display],
	['gc', X.GC],
	['stipple', X.Pixmap]
	)
	
X.Display.SetTSOrigin = X.Callable(
	'XSetTSOrigin', int,
	['self', X.Display],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer]
	)
	
X.Display.SetFont = X.Callable(
	'XSetFont', int,
	['self', X.Display],
	['gc', X.GC],
	['font', X.Font]
	)
	
X.Display.SetSubwindowMode = X.Callable(
	'XSetSubwindowMode', int,
	['self', X.Display],
	['gc', X.GC],
	['mode', X.Cardinal]
	)
	
X.Display.SetGraphicsExposures = X.Callable(
	'XSetGraphicsExposures', int,
	['self', X.Display],
	['gc', X.GC],
	['expose', X.BOOL, True]
	)
	
X.Display.SetClipOrigin = X.Callable(
	'XSetClipOrigin', int,
	['self', X.Display],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer]
	)
	
X.Display.SetClipMask = X.Callable(
	'XSetClipMask', int,
	['self', X.Display],
	['gc', X.GC],
	['mask', X.Pixmap]
	)
	
X.Display.SetClipRectangles = X.Callable(
	'XSetClipRectangles', int,
	['self', X.Display],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['rectangles', X.ListOf(X.Rectangle)],
	['n_rectangles', X.Integer],
	['ordering', X.Cardinal]
	)
	
