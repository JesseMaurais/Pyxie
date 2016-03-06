import X11 as X, bit, ctypes

class StandardColormap(ctypes.Structure):
	_fields_ = [
		('colormap', X.Colormap),
		('red_max', X.INT),
		('red_mult', X.INT),
		('green_max', X.INT),
		('green_mult', X.INT),
		('blue_max', X.INT),
		('blue_mult', X.INT),
		('base_pixel', X.Pixel),
		('visualid', X.VisualID),
		('killid', X.ID)
		]
		
ReleaseByFreeingColormap = X.ID(1) # killid

	
X.Display.SetStandardColormap = X.Callable(
	'XSetStandardColormap', None,
	['self', X.Display],
	['window', X.Window],
	['map', X.ByRef(StandardColormap)],
	['property', X.Atom]
	)

X.Display.GetStandardColormap = X.Callable(
	'XGetStandardColormap', X.Status,
	['self', X.Display],
	['window', X.Window],
	['standard', X.ByRef(StandardColormap)],
	['property', X.Atom]
	)

X.Display.SetRGBColormaps = X.Callable(
	'XSetRGBColormaps', None,
	['self', X.Display],
	['window', X.Window],
	['maps', X.ListOf(StandardColormap)],
	['nmaps', X.Integer],
	['property', X.Atom]
	)

X.Display.GetRGBColormaps = X.Callable(
	'XGetRGBColormaps', X.Status,
	['window', X.Window],
	['maps_return', X.ArrayOf(StandardColormap)],
	['nmaps_return', X.INT32],
	['property', X.Atom]
	)
	
X.Display.SetWMColormapWindows = X.Callable(
	'XSetWMColormapWindows', X.Status,
	['self', X.Display],
	['window', X.Window],
	['windows', X.ListOf(X.Window)],
	['nwindows', X.Integer]
	)
	
X.Display.GetWMColormapWindows = X.Callable(
	'XGetWMColormapWindows', X.Status,
	['self', X.Display],
	['window', X.Window],
	['windows_return', X.ArrayOf(X.Window)],
	['nwindows_return', X.INT]
	)

X.Display.StoreName = X.Callable(
	'XStoreName', int,
	['self', X.Display],
	['window', X.Window],
	['name', X.String]
	)
	
X.Display.FetchName = X.Callable(
	'XFetchName', X.Status,
	['self', X.Display],
	['window', X.Window],
	['name_return', X.STRING8]
	)

X.Window.name = property(lambda wnd: wnd.FetchName(), lambda wnd, s: wnd.StoreName(s))

X.Display.SetIconName = X.Callable(
	'XSetIconName', int,
	['self', X.Display],
	['window', X.Window],
	['name', X.String]
	)

X.Display.GetIconName = X.Callable(
	'XGetIconName', X.Status,
	['self', X.Display],
	['window', X.Window],
	['name_return', X.String]
	)

X.Display.SetTransientForHint = X.Callable(
	'XSetTransientForHint', int,
	['self', X.Display],
	['window', X.Window],
	['trans', X.Window]
	)

X.Display.GetTransientForHint = X.Callable(
	'XGetTransientForHint', X.Status,
	['self', X.Display],
	['window', X.Window],
	['trans_return', X.Window]
	)

X.Display.SetWMProtocols = X.Callable(
	'XSetWMProtocols', X.Status,
	['self', X.Display],
	['window', X.Window],
	['protocols', X.ListOf(X.Atom)],
	['count', X.Integer, 1]
	)

X.Display.GetWMProtocols = X.Callable(
	'XGetWMProtocols', X.Status,
	['self', X.Display],
	['window', X.Window],
	['protocols_return', X.ArrayOf(X.Atom)],
	['count_return', X.INT]
	)

X.Display.SetCommand = X.Callable(
	'XSetCommand', int,
	['self', X.Display],
	['window', X.Window],
	['argv', X.ListOf(X.String)],
	['argc', X.Integer]
	)

X.Display.GetCommand = X.Callable(
	'XGetCommand', X.Status,
	['self', X.Display],
	['window', X.Window],
	['argv_return', X.ArrayOf(X.String)],
	['argc_return', X.INT]
	)

