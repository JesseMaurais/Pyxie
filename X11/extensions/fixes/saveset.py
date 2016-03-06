import X11 as X
from X11.extensions.fixes import Callable

X.Display.FixesChangeSaveSet = Callable(
	'XFixesChangeSaveSet', None,
	['self', X.Display],
	['window', X.Window],
	['mode', X.Cardinal],
	['target', X.Cardinal],
	['unmap', X.BOOL, False]
	)
