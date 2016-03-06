import X11 as X
from X11.utility import Callable

X.Display.DrawRoundedRectangle = Callable(
	'XmuDrawRoundedRectangle', None,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer],
	['ewidth', X.Integer],
	['eheight', X.Integer]
	)

X.Display.FillRoundedRectangle = Callable(
	'XmuFillRoundedRectangle', None,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer],
	['ewidth', X.Integer],
	['eheight', X.Integer]
	)

X.Display.DrawLogo = Callable(
	'XmuDrawLogo', None,
	['self', X.Display],
	['drawable', X.Drawable],
	['foreground', X.GC],
	['background', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer]
	)

