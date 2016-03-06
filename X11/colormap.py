import X11 as X

X.Display.CreateColormap = X.Callable(
	'XCreateColormap', X.Colormap,
	['self', X.Display],
	['window', X.Window],
	['visual', X.Visual, X.CopyFromParent],
	['alloc', X.BOOL, False]
	)
	
X.Display.FreeColormap = X.Callable(
	'XFreeColormap', int,
	['self', X.Display],
	['colormap', X.Colormap]
	)

X.Display.CopyColormapAndFree = X.Callable(
	'XCopyColormapAndFree', X.Colormap,
	['self', X.Display],
	['colormap', X.Colormap]
	)
	
X.Display.InstallColormap = X.Callable(
	'XInstallColormap', int,
	['self', X.Display],
	['colormap', X.Colormap]
	)
	
X.Display.UninstallColormap = X.Callable(
	'XUninstallColormap', int,
	['self', X.Display],
	['colormap', X.Colormap]
	)
	
X.Display.ListInstalledColormaps = X.Callable(
	'XListInstalledColormaps', X.ArrayOf(X.Colormap),
	['self', X.Display],
	['window', X.Window],
	['count', X.ByRef(X.INT)]
	)

def InstalledColormapsList(window):
	n = X.INT()
	colors = window.ListInstalledColormaps(n)
	for i in range(n.value):
		yield colors[i]
	X.Free(colors)

X.Window.installed_colormaps = property(InstalledColormapsList)	

X.Display.AllocColor = X.Callable(
	'XAllocColor', X.Status,
	['self', X.Display],
	['colormap', X.Colormap],
	['screen', X.ByRef(X.Color)]
	)
	
X.Display.AllocNamedColor = X.Callable(
	'XAllocNamedColor', X.Status,
	['self', X.Display],
	['colormap', X.Colormap],
	['name', X.String],
	['return_screen', X.Color],
	['return_exact', X.Color]
	)
	
X.Display.FreeColors = X.Callable(
	'XFreeColors', int,
	['self', X.Display],
	['colormap', X.Colormap],
	['pixels', X.ListOf(X.Pixel)],
	['npixels', X.Integer],
	['planes', X.Bitmask]
	)

X.Display.AllocColorCells = X.Callable(
	'XAllocColorCells', X.Status,
	['self', X.Display],
	['colormap', X.Colormap],
	['contiguous', X.BOOL, False],
	['return_plane_masks', X.Bitmask],
	['nplanes', X.Integer],
	['return_pixels', X.Pixel],
	['npixels', X.Integer]
	)

X.Display.AllocColorPlanes = X.Callable(
	'XAllocColorPlanes', X.Status,
	['self', X.Display],
	['colormap', X.Colormap],
	['contiguous', X.BOOL, False],
	['return_pixels', X.AddressOf(X.Pixel)],
	['ncolors', X.Integer],
	['nreds', X.Integer],
	['ngreens', X.Integer],
	['nblues', X.Integer],
	['return_red_mask', X.Bitmask],
	['return_green_mask', X.Bitmask],
	['return_blue_mask', X.Bitmask]
	)

X.Display.LookupColor = X.Callable(
	'XLookupColor', X.Status,
	['self', X.Display],
	['colormap', X.Colormap],
	['name', X.String],
	['return_exact', X.Color],
	['return_screen', X.Color]
	)

X.Display.ParseColor = X.Callable(
	'XParseColor', X.Status,
	['self', X.Display],
	['colormap', X.Colormap],
	['spec', X.String],
	['return_exact', X.Color]
	)

X.Display.QueryColor = X.Callable(
	'XQueryColor', int,
	['self', X.Display],
	['colormap', X.Colormap],
	['in_out', X.ByRef(X.Color)]
	)
	
X.Display.QueryColors = X.Callable(
	'XQueryColors', int,
	['self', X.Display],
	['colormap', X.Colormap],
	['in_out', X.AddressOf(X.Color)],
	['ncolors', X.Integer]
	)
	
X.Display.StoreColor = X.Callable(
	'XStoreColor', int,
	['self', X.Display],
	['colormap', X.Colormap],
	['color', X.ByRef(X.Color)]
	)

X.Display.StoreColors = X.Callable(
	'XStoreColors', int,
	['self', X.Display],
	['colormap', X.Colormap],
	['colors', X.ListOf(X.Color)],
	['ncolors', X.Integer]
	)
	
X.Display.StoreNamedColor = X.Callable(
	'XStoreNamedColor', int,
	['self', X.Display],
	['colormap', X.Colormap],
	['colorname', X.String],
	['pixel', X.Pixel],
	['flags', X.Bitmask, X.RGB]
	)


### Sugar #####################################################


def LookupColor(colormap, name):
	'Assume unknown colormap attributes refer to color names'
	lookup = X.CurrentDisplayAttribute(colormap, 'AllocNamedColor')
	color, exact = lookup(name)
	setattr(colormap, name, color.pixel)
	return color.pixel

X.Colormap.__getattr__ = LookupColor



