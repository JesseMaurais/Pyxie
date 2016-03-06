import X11 as X, ctypes

X.Display.ProcessInternalConnection = X.Callable(
	'XProcessInternalConnection', None,
	['self', X.Display],
	['fd', X.Integer]
	)
	
X.Display.InternalConnectionNumbers = X.Callable(
	'XInternalConnectionNumbers', X.Status,
	['self', X.Display],
	['return_fds', ArrayOf(X.INT)],
	['return_nfds', X.INT]
	)
	
def InternalConnectionNumbers(display):
	fds, n = display.InternalConnectionNumbers()
	for i in range(n.value):
		yield fds[i]
	X.Free(fds)
	
X.Display.internal_connection_numbers = property(InternalConnectionNumbers)

Watch = ctypes.CFUNCTYPE(None, X.Display, X.Pointer, X.INT, X.BOOL, X.Pointer)

X.Display.AddConnectionWatch = X.Callable(
	'XAddConnectionWatch', X.Status,
	['self', X.Display],
	['procedure', Watch],
	['userdata', X.Pointer, None]
	)
	
X.Display.RemoveConnectionWatch = X.Callable(
	'XRemoveConnectionWatch', X.Status,
	['self', X.Display],
	['procedure', Watch],
	['userdata', X.Pointer, None]
	)

