import X11 as X, bit

Mode = bit.enum('DestroyAll RetainPermanent RetainTemporary')

X.Display.SetCloseDownMode = X.Callable(
	'XSetCloseDownMode', int,
	['self', X.Display],
	['mode', X.Cardinal, Mode.DestroyAll]
	)
	
X.Display.KillClient = X.Callable(
	'XKillClient', int,
	['self', X.Display],
	['resource', X.ID]
	)

