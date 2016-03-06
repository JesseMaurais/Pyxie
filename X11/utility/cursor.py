import X11 as X
from X11.utility import Callable

X.Display.CursorNameToIndex = Callable(
	'XmuCursorNameToIndex', int,
	['name', X.String]
	)

