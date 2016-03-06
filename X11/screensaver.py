import X11 as X, bit

Blanking = bit.enum('DontPrefer Prefer Default')

Exposures = bit.enum('DontAllow Allow Default')

X.Display.SetScreenSaver = X.Callable(
	'XSetScreenSaver', int,
	['self', X.Display],
	['timeout', X.Integer],
	['interval', X.Integer],
	['prefer_blanking', X.Cardinal, Blanking.Default],
	['allow_exposures', X.Cardinal, Exposures.Default]
	)
	
X.Display.GetScreenSaver = X.Callable(
	'XGetScreenSaver', int,
	['self', X.Display],
	['return_timeout', X.INT],
	['return_interval', X.INT],
	['return_prefer_blanking', X.CARD],
	['return_allow_exposures', X.CARD]
	)

Mode = bit.enum('Reset Activate')
	
X.Display.ForceScreenSaver = X.Callable(
	'XForceScreenSaver', int,
	['self', X.Display],
	['mode', X.Cardinal, Mode.Activate]
	)
	
X.Display.ResetScreenSaver = X.Callable(
	'XResetScreenSaver', int,
	['self', X.Display]
	)
	
X.Display.ActivateScreenSaver = X.Callable(
	'XActivateScreenSaver', int,
	['self', X.Display]
	)

