import X11 as X

X.Callable.lib.XInitThreads()

X.Display.Lock = X.Callable(
	'XLockDisplay', None,
	['self', X.Display]
	)

X.Display.Unlock = X.Callable(
	'XUnlockDisplay', None,
	['self', X.Display]
	)

