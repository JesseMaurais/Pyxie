import X11 as X

Create = X.Callable('XCreateRegion', X.Region)

Polygon = X.Callable(
	'XPolygonRegion', X.Region,
	['points', X.ListOf(X.Point)],
	['n_points', X.Integer],
	['fill_rule', X.Cardinal]
	)
	
X.Display.SetRegion = X.Callable(
	'XSetRegion', int,
	['self', X.Display],
	['gc', X.GC],
	['region', X.Region]
	)
	
X.Rectangle.__or__ = X.Callable(
	'XUnionRectWithRegion', int,
	['self', X.AddressOf(X.Rectangle)],
	['region', X.Region],
	['return', X.Region]
	)

X.Region.__del__ = X.Callable(
	'XDestroyRegion', int,
	['self', X.Region]
	)

X.Region.__nonzero__ = X.Callable(
	'XEmptyRegion', bool,
	['self', X.Region]
	)
	
X.Region.__eq__ = X.Callable(
	'XEqualRegion', bool,
	['self', X.Region],
	['other', X.Region]
	)

X.Region.__and__ = X.Callable(
	'XIntersectRegion', int,
	['self', X.Region],
	['other', X.Region],
	['return', X.Region]
	)
	
X.Region.__or__ = X.Callable(
	'XUnionRegion', int,
	['self', X.Region],
	['other', X.Region],
	['return', X.Region]
	)
	
X.Region.__xor__ = X.Callable(
	'XXorRegion', int,
	['self', X.Region],
	['other', X.Region],
	['return', X.Region]
	)
	
X.Region.__sub__ = X.Callable(
	'XSubtractRegion', int,
	['self', X.Region],
	['other', X.Region],
	['return', X.Region]
	)
	
X.Region.Offset = X.Callable(
	'XOffsetRegion', int,
	['self', X.Region],
	['x', X.Integer],
	['y', X.Integer]
	)
	
X.Region.Shrink = X.Callable(
	'XShrinkRegion', int,
	['self', X.Region],
	['x', X.Integer],
	['y', X.Integer]
	)

X.Region.ClipBox = X.Callable(
	'XClipBox', int,
	['self', X.Region],
	['return', X.Rectangle]
	)
	
X.Region.ContainsPoint = X.Callable(
	'XPointInRegion', bool,
	['self', X.Region],
	['x', X.Integer],
	['y', X.Integer]
	)
	
X.Region.ContainsRectangle = X.Callable(
	'XRectInRegion', int,
	['self', X.Region],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer]
	)

def Contains(region, shape):
	if isinstance(shape, X.Point):
		return region.ContainsPoint(shape.x, shape.y)
	if isinstance(shape, X.Rectangle):
		return region.ContainsRectangle(shape.x, shape.y, shape.width, shape.height)
	raise TypeError('Shape must be either Point or Rectangle')

X.Region.__contains__ = Contains



