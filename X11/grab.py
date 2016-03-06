import X11 as X, bit

Status = bit.enum(
	"""
	Success
	AlreadyGrabbed
	InvalidTime
	NotViewable
	Frozen
	"""
	)

X.Display.GrabServer = X.Callable(
	'XGrabServer', int,
	['self', X.Display]
	)
	
X.Display.UngrabServer = X.Callable(
	'XUngrabServer', int,
	['self', X.Display]
	)

X.Display.GrabPointer = X.Callable(
	'XGrabPointer', int,
	['self', X.Display],
	['grab_window', X.Window],
	['owner_events', X.BOOL, False],
	['event_mask', X.Bitmask, None],
	['sync_pointer', X.BOOL, False],
	['sync_keyboard', X.BOOL, False],
	['confine_to', X.Window, None],
	['cursor', X.Cursor, None],
	['time', X.Time, X.CurrentTime]
	)
	
X.Display.UngrabPointer = X.Callable(
	'XUngrabPointer', int,
	['self', X.Display],
	['time', X.Time, X.CurrentTime]
	)
	
X.Display.GrabButton = X.Callable(
	'XGrabButton', int,
	['self', X.Display],
	['button', X.Integer],
	['modifiers', X.Bitmask],
	['grab_window', X.Window],
	['owner_events', X.BOOL, False],
	['event_mask', X.Bitmask, None],
	['sync_pointer', X.BOOL, False],
	['sync_keyboard', X.BOOL, False],
	['confine_to', X.Window, None],
	['cursor', X.Cursor, None]
	)
	
X.Display.UngrabButton = X.Callable(
	'XUngrabButton', int,
	['self', X.Display],
	['button', X.Integer],
	['modifiers', X.Bitmask],
	['grab_window', X.Window]
	)

X.Display.GrabKeyboard = X.Callable(
	'XGrabKeyboard', int,
	['self', X.Display],
	['grab_window', X.Window],
	['owner_events', X.BOOL, False],
	['sync_pointer', X.BOOL, False],
	['sync_keyboard', X.BOOL, False],
	['time', X.Time, X.CurrentTime]
	)
	
X.Display.UngrabKeyboard = X.Callable(
	'XUngrabKeyboard', int,
	['self', X.Display],
	['time', X.Time, X.CurrentTime]
	)
	
X.Display.GrabKey = X.Callable(
	'XGrabKey', int,
	['self', X.Display],
	['keycode', X.KeyCode],
	['modifiers', X.Bitmask],
	['grab_window', X.Window],
	['owner_events', X.BOOL, False],
	['sync_pointer', X.BOOL, False],
	['sync_keyboard', X.BOOL, False]
	)
	
X.Display.UngrabKey = X.Callable(
	'XUngrabKey', int,
	['self', X.Display],
	['keycode', X.KeyCode],
	['modifiers', X.Bitmask],
	['grab_window', X.Window]
	)
	
