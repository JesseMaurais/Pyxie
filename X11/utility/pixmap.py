import X11 as X
from X11.utility import Callable

X.Display.CreatePixmapFromBitmap = Callable(
	'XmuCreatePixmapFromBitmap', X.Pixmap,
	['self', X.Display],
	['drawable', X.Drawable],
	['bitmap', X.Pixmap],
	['width', X.Integer],
	['height', X.Integer],
	['depth', X.Integer],
	['foreground', X.Pixel],
	['background', X.Pixel]
	)

X.Screen.CreateStipplePixmap = Callable(
	'XmuCreateStippledPixmap', X.Pixmap,
	['self', X.Screen],
	['foreground', X.Pixel],
	['background', X.Pixel],
	['depth', X.Integer, 24]
	)

X.Screen.ReleaseStippledPixmap = Callable(
	'XmuReleaseStippledPixmap', None,
	['self', X.Screen],
	['pixmap', X.Pixmap]
	)

