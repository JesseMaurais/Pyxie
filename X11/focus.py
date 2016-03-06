import X11 as X, bit

RevertTo = bit.enum('None PointerRoot Parent')

X.Display.SetInputFocus = X.Callable(
	'XSetInputFocus', int,
	['self', X.Display],
	['focus', X.Window],
	['revert_to', X.Cardinal, None],
	['time', X.Time, X.CurrentTime]
	)
	
X.Display.GetInputFocus = X.Callable(
	'XGetInputFocus', int,
	['self', X.Display],
	['return_focus', X.Window],
	['return_revert_to', X.CARD]
	)
	

