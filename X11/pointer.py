import X11 as X
	
X.Display.ChangeActivePointerGrab = X.Callable(
	'XChangeActivePointerGrab', int,
	['self', X.Display],
	['event_mask', X.Bitmask],
	['cursor', X.Cursor],
	['time', X.Time, X.CurrentTime]
	)

X.Display.ChangePointerControl = X.Callable(
	'XChangePointerControl', int,
	['self', X.Display],
	['do_accel', X.BOOL],
	['do_threshold', X.BOOL],
	['accel_numerator', X.Integer],
	['accel_denominator', X.Integer],
	['threshold', X.Integer]
	)
	
X.Display.GetPointerControl = X.Callable(
	'XGetPointerControl', int,
	['self', X.Display],
	['return_accel_numerator', X.INT],
	['return_accel_denominator', X.INT],
	['return_threshold', X.INT]
	)

X.Display.WarpPointer = X.Callable(
	'XWarpPointer', int,
	['self', X.Display],
	['from', X.Window],
	['to', X.Window],
	['from_x', X.Integer],
	['from_y', X.Integer],
	['from_width', X.Integer],
	['from_height', X.Integer],
	['to_x', X.Integer],
	['to_y', X.Integer]
	)
	
X.Display.QueryPointer = X.Callable(
	'XQueryPointer', bool,
	['self', X.Display],
	['window', X.Window],
	['return_root', X.Window],
	['return_child', X.Window],
	['return_root_x', X.Integer],
	['return_root_y', X.Integer],
	['return_window_x', X.Integer],
	['return_window_y', X.Integer],
	['return_modifiers', X.Bitmask]
	)
	
X.Display.SetPointerMapping = X.Callable(
	'XSetPointerMapping', int,
	['self', X.Display],
	['maps', X.ArrayOf(X.BYTE)],
	['n_maps', X.Integer]
	)
	
X.Display.GetPointerMapping = X.Callable(
	'XGetPointerMapping', int,
	['self', X.Display],
	['maps', X.ArrayOf(X.BYTE)],
	['n_maps', X.Integer]
	)

