import X11 as X, ctypes

X.Display.Sync = X.Callable(
	'XSync', int,
	['self', X.Display],
	['discard_events', X.BOOL, False]
	)
	
X.Display.Synchronize = X.Callable(
	'XSynchronize', int,
	['self', X.Display],
	['onoff', X.BOOL, True]
	)

AfterFunction = ctypes.CFUNCTYPE(X.INT, X.Display)

X.Display.SetAfterFunction = X.Callable(
	'XSetAfterFunction', AfterFunction,
	['self', X.Display],
	['procedure', AfterFunction]
	)
	
