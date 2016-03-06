import X11 as X

Callable = X.Wrapper('Xcomposite')

X.Display.RedirectWindow = Callable(
	'XCompositeRedirectWindow', None,
	['self', X.Display],
	['window', X.Window],
	['manual', X.BOOL, False]
	)
	
X.Display.RedirectSubwindows = Callable(
	'XCompositeRedirectSubwindows', None,
	['self', X.Display],
	['window', X.Window],
	['manual', X.BOOL, False]
	)
	
X.Display.UnredirectWindow = Callable(
	'XCompositeRedirectSubwindows', None,
	['self', X.Display],
	['window', X.Window],
	['manual', X.BOOL, False]
	)
	
X.Display.UnredirectSubwindows = Callable(
	'XCompositeRedirectSubwindows', None,
	['self', X.Display],
	['window', X.Window],
	['manual', X.BOOL, False]
	)
	
X.Display.CreateRegionFromBorderClip = Callable(
	'XCompositeCreateRegionFromBorderClip', X.ID,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.NameWindowPixmap = Callable(
	'XCompositeNameWindowPixmap', X.Pixmap,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.GetOverlayWindow = Callable(
	'XCompositeGetOverlayWindow', X.Window,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.ReleaseOverlayWindow = Callable(
	'XCompositeReleaseOverlayWindow', None,
	['self', X.Display],
	['window', X.Window]
	)
	
