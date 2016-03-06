import X11 as X

X.Display.StoreBytes = X.Callable(
	'XStoreBytes', int,
	['self', X.Display],
	['bytes', X.STRING8],
	['nbytes', X.Integer]
	)
	
X.Display.FetchBytes = X.Callable(
	'XFetchBytes', X.STRING8,
	['self', X.Display],
	['nbytes', X.ByRef(X.INT)]
	)
	
X.Display.StoreBuffer = X.Callable(
	'XStoreBuffer', int,
	['self', X.Display],
	['bytes', X.STRING8],
	['nbytes', X.Integer],
	['buffer', X.Cardinal]
	)
	
X.Display.FetchBuffer = X.Callable(
	'XFetchBuffer', X.STRING8,
	['self', X.Display],
	['nbytes', X.ByRef(X.INT)],
	['buffer', X.Cardinal]
	)
	
X.Display.RotateBuffers = X.Callable(
	'XRotateBuffers', int,
	['self', X.Display],
	['rotate', X.Integer]
	)

