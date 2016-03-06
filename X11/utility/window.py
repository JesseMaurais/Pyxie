import X11 as X
from X11.hint import SizeHints
from X11.utility import Callable

X.Display.ClientWindow = Callable(
	'XmuClientWindow', X.Window,
	['self', X.Display],
	['window', X.Window]
	)

X.Display.UpdateMapHints = Callable(
	'XmuUpdateMapHints', bool,
	['self', X.Display],
	['window', X.Window],
	['hints', X.AddressOf(SizeHints), None]
	)

X.Display.ScreenOfWindow = Callable(
	'XmuScreenOfWindow', X.Screen,
	['self', X.Display],
	['window', X.Window]
	)

# Sugar

X.Window.client = property(lambda window: window.ClientWindow())

X.Window.screen = property(lambda window: window.ScreenOfWindow())

