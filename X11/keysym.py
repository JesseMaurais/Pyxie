import X11 as X

X.Display.KeycodeToKeysym = X.Callable(
	'XKeycodeToKeysym', X.KeySym,
	['self', X.Display],
	['keycode', X.KeyCode],
	['index', X.Integer]
	)
	
X.Display.KeysymToKeycode = X.Callable(
	'XKeysymToKeycode', X.KeyCode,
	['self', X.Display],
	['keysym', X.KeySym]
	)
	
X.KeySym.ConvertCase = X.Callable(
	'XConvertCase', None,
	['self', X.KeySym],
	['lower_return', X.KeySym],
	['upper_return', X.KeySym]
	)
	
X.KeySym.__str__ = X.Callable(
	'XKeysymToString', X.STRING8,
	['self', X.KeySym]
	)
	
X.String.keysym = property(X.Callable(
	'XStringToKeysym', X.KeySym,
	['self', X.String]
	))

