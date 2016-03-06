import X11 as X
from X11.extensions.fixes import Callable

X.Display.HideCursor = Callable(
	'XFixesHideCursor', None,
	['self', X.Display],
	['window', X.Window]
	)

X.Display.ShowCursor = Callable(
	'XFixesShowCursor', None,
	['self', X.Display],
	['window', X.Window]
	)

X.Display.SetCursorName = Callable(
	'XFixesSetCursorName', None,
	['self', X.Display],
	['cursor', X.Cursor],
	['name', X.String]
	)

X.Display.GetCursorName = Callable(
	'XFixesGetCursorName', X.STRING8,
	['self', X.Display],
	['cursor', X.Cursor],
	['atom', X.ByRef(Atom)]
	)

X.Display.ChangeCursor = Callable(
	'XFixesChangeCursor', None,
	['self', X.Display],
	['src', X.Cursor],
	['dst', X.Cursor]
	)

X.Display.ChangeCursorByName = Callable(
	'XFixesChangeCursorByName', None,
	['self', X.Display],
	['src', X.Cursor],
	['dst_name', X.String]
	)

X.Display.SelectCursorInput = Callable(
	'XFixesSelectCursorInput', None,
	['self', X.Display],
	['window', X.Window],
	['mask', X.Bitmask]
	)
	
class CursorImage(X.Structure):
	_fields_ = [
		('x', X.INT16),
		('y', X.INT16),
		('width', X.INT16),
		('height', X.INT16),
		('xhot', X.INT16),
		('yhot', X.INT16),
		('cursor_serial', X.INT32),
		('pixels', X.ArrayOf(X.Pixel)),
		('atom', X.Atom),
		('name', X.STRING8)
		]
		
X.Display.GetCursorImage = Callable(
	'XFixesGetCursorImage', X.AddressOf(CursorImage),
	['self', X.Display]
	)
	
class CursorNotify(X.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('subtype', X.CARD),
		('cursor_serial', X.INT),
		('timestamp', X.Time),
		('cursor_name', X.Atom)
		]
		
from X11.event import Event
Event._fields_.append(('xcursor', CursorNotify))

