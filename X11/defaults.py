import X11 as X

X.Display.RootWindow = X.Callable(
	'XRootWindow', X.Window,
	['self', X.Display],
	['screen', X.Integer, 0]
	)

X.Display.Screen = X.Callable(
	'XScreenOfDisplay', X.Screen,
	['self', X.Display],
	['screen', X.Integer, 0]
	)

X.Display.Visual = X.Callable(
	'XDefaultVisual', X.Visual,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
X.Display.GC = X.Callable(
	'XDefaultGC', X.GC,
	['self', X.Display],
	['screen', X.Integer, 0]
	)

X.Display.Colormap = X.Callable(
	'XDefaultColormap', X.Colormap,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
X.Display.Depth = X.Callable(
	'XDefaultDepth', int,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
X.Display.ListDepths = X.Callable(
	'XListDepths', ArrayOf(X.INT),
	['self', X.Display],
	['screen', X.Integer, 0],
	['count', X.ByRef(X.INT)]
	)
	
X.Display.Planes = X.Callable(
	'XDisplayPlanes', int,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
X.Display.Black = X.Callable(
	'XBlackPixel', X.Pixel,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
X.Display.White = X.Callable(
	'XWhitePixel', X.Pixel,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
X.Display.Cells = X.Callable(
	'XDisplayCells', int,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
X.Display.Width = X.Callable(
	'XDisplayWidth', int,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
X.Display.Height = X.Callable(
	'XDisplayHeight', int,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
X.Display.WidthMM = X.Callable(
	'XDisplayWidthMM', int,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
X.Display.HeightMM = X.Callable(
	'XDisplayHeightMM', int,
	['self', X.Display],
	['screen', X.Integer, 0]
	)
	
