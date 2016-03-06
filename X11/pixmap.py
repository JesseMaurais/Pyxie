import X11 as X

X.Display.CreatePixmap = X.Callable(
	'XCreatePixmap', X.Pixmap,
	['self', X.Display],
	['drawable', X.Drawable],
	['width', X.Integer, 1],
	['height', X.Integer, 1],
	['depth', X.Integer, 1]
	)
	
X.Display.FreePixmap = X.Callable(
	'XFreePixmap', int,
	['self', X.Display],
	['pixmap', X.Pixmap]
	)
	
X.Display.ListPixmapFormats = X.Callable(
	'XListPixmapFormats', X.ArrayOf(X.PixmapFormat),
	['self', X.Display],
	['count', X.ByRef(X.INT)]
	)
	
def ListPixmapFormats(display):
	count = X.INT()
	formats = display.ListPixmapFormats(count)
	lst = [formats[i] for i in range(count.value)]
	X.Free(formats)
	return lst
	
X.Display.pixmap_formats = property(ListPixmapFormats)

