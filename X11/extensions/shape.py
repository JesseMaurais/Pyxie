import X11 as X, ctypes
from X11 import bit
from ext import Callable

X.Display.QueryShapeExtension = Callable(
	'XShapeQueryExtension', bool,
	['self', X.Display],
	['return_event', X.CARD],
	['return_error', X.CARD]
	)

X.Display.QueryShapeVersion = Callable(
	'XShapeQueryVersion', X.Status,
	['self', X.Display],
	['return_major_version', X.INT],
	['return_minor_version', X.INT]
	)
	
Op = bit.enum(
	"""
	Set
	Union
	Intersect
	Subtract
	Invert
	"""
	)

Kind = bit.enum(
	"""
	Bounding
	Clip
	Input
	"""
	)

X.Display.CombineRegion = Callable(
	'XShapeCombineRegion', None,
	['display', X.Display],
	['target', X.Window],
	['kind', X.Cardinal],
	['xoff', X.Integer],
	['yoff', X.Integer],
	['region', X.Region],
	['op', X.Cardinal]
	)

X.Display.CombineRectangles = Callable(
	'XShapeCombineRectangles', None,
	['self', X.Display],
	['target', X.Window],
	['kind', X.Cardinal],
	['xoff', X.Integer],
	['yoff', X.Integer],
	['rects', X.ListOf(X.Rectangle)],
	['n_rects', X.Integer],
	['op', X.Cardinal],
	['ordering', X.Cardinal]
	)

X.Display.CombineMask = Callable(
	'XShapeCombineMask', None,
	['self', X.Display],
	['target', X.Window],
	['kind', X.Cardinal],
	['xoff', X.Integer],
	['yoff', X.Integer],
	['mask', X.Pixmap],
	['op', X.Cardinal]
	)

X.Display.CombineShape = Callable(
	'XShapeCombineShape', None,
	['self', X.Display],
	['target', X.Window],
	['kind', X.Cardinal],
	['xoff', X.Integer],
	['yoff', X.Integer],
	['source', X.Window],
	['source_kind', X.Cardinal],
	['op', X.Cardinal]
	)

X.Display.OffsetShape = Callable(
	'XShapeOffsetShape', None,
	['self', X.Display],
	['target', X.Window],
	['kind', X.Cardinal],
	['xoff', X.Integer],
	['yoff', X.Integer]
	)

X.Display.QueryExtents = Callable(
	'XShapeQueryExtents', X.Status,
	['self', X.Display],
	['window', X.Window],
	['return_shaped', X.BOOL],
	['return_x', X.INT],
	['return_y', X.INT],
	['return_width', X.INT],
	['return_height', X.INT],
	['return_clip_shaped', X.BOOL],
	['return_clip_x', X.INT],
	['return_clip_y', X.INT],
	['return_clip_width', X.INT],
	['return_clip_height', X.INT]
	)

X.Display.ShapeSelectInput = Callable(
	'XShapeSelectInput', None,
	['self', X.Display],
	['window', X.Window],
	['mask', X.Bitmask]
	)

X.Display.InputSelected = Callable(
	'XShapeInputSelected', X.Bitmask,
	['self', X.Display],
	['window', X.Window]
	)

X.Display.GetRectangles = Callable(
	'XShapeGetRectangles', X.ArrayOf(X.Rectangle),
	['self', X.Display],
	['window', X.Window],
	['kind', X.Cardinal],
	['count', X.ByRef(X.INT)],
	['ordering', X.ByRef(X.INT)]
	)
	
	
class Event(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('kind', X.CARD),
		('x', X.INT),
		('y', X.INT),
		('width', X.INT),
		('height', X.INT),
		('time', X.Time),
		('shaped', X.BOOL)
		]

from X11.event import Event
Event._fields_.append(('xshape', Event))

