import X11 as X, ctypes

X.Display.GetGeometry = X.Callable(
	'XGetGeometry', X.Status,
	['self', X.Display],
	['drawable', X.Drawable],
	['return_root', X.Window],
	['return_x', X.INT],
	['return_y', X.INT],
	['return_width', X.INT],
	['return_height', X.INT],
	['return_border_width', X.INT],
	['return_depth', X.INT]
	)

X.Display.CopyArea = X.Callable(
	'XCopyArea', int,
	['self', X.Display],
	['src', X.Drawable],
	['dst', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer],
	['dst_x', X.Integer, 0],
	['dst_y', X.Integer, 0]
	)
	
X.Display.CopyPlane = X.Callable(
	'XCopyPlane', int,
	['self', X.Display],
	['src', X.Drawable],
	['dst', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer],
	['dst_x', X.Integer, 0],
	['dst_y', X.Integer, 0],
	['plane', X.Integer]
	)

X.Display.DrawArc = X.Callable(
	'XDrawArc', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer],
	['angle1', X.Integer],
	['angle2', X.Integer]
	)

X.Display.DrawArcs = X.Callable(
	'XDrawArc', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['arcs', X.ListOf(X.Arc)],
	['n_arcs', X.Integer]
	)

X.Display.DrawLine = X.Callable(
	'XDrawLine', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x1', X.Integer],
	['y1', X.Integer],
	['x2', X.Integer],
	['y2', X.Integer]
	)

X.Display.DrawLines = X.Callable(
	'XDrawLines', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['points', X.ListOf(X.Point)],
	['n_points', X.Integer],
	['mode', X.Cardinal]
	)

X.Display.DrawPoint = X.Callable(
	'XDrawPoint', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer]
	)

X.Display.DrawPoints = X.Callable(
	'XDrawPoints', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['points', X.ListOf(X.Point)],
	['n_points', X.Integer],
	['mode', X.Cardinal]
	)

X.Display.DrawRectangle = X.Callable(
	'XDrawRectangle', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer]
	)

X.Display.DrawRectangles = X.Callable(
	'XDrawRectangles', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['rectangles', X.ListOf(X.Rectangle)],
	['n_rectangles', X.Integer]
	)

X.Display.DrawSegments = X.Callable(
	'XDrawSegments', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['segments', X.ListOf(X.Segment)],
	['n_segments', X.Integer]
	)

X.Display.DrawString = X.Callable(
	'XDrawString', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['string', X.String],
	['length', X.Integer]
	)

X.Display.DrawString16 = X.Callable(
	'XDrawString16', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['string', X.STRING16],
	['length', X.Integer]
	)
	
X.Display.DrawImageString = X.Callable(
	'XDrawImageString', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['string', X.STRING8],
	['length', X.Integer]
	)

X.Display.DrawImageString16 = X.Callable(
	'XDrawImageString', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['string', X.STRING16],
	['length', X.Integer]
	)

X.Display.FillArc = X.Callable(
	'XFillArc', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer],
	['angle1', X.Integer],
	['angle2', X.Integer]
	)

X.Display.FillArcs = X.Callable(
	'XFillArc', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['arcs', X.ListOf(X.Arc)],
	['n_arcs', X.Integer]
	)

X.Display.FillPolygon = X.Callable(
	'XFillPolygon', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['points', X.ListOf(X.Point)],
	['n_points', X.Integer],
	['shape', X.Cardinal],
	['mode', X.Cardinal]
	)

X.Display.FillRectangle = X.Callable(
	'XFillRectangle', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer]
	)

X.Display.FillRectangles = X.Callable(
	'XFillRectangles', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['rectangles', X.ListOf(X.Rectangle)],
	['n_rectangles', X.Integer]
	)

