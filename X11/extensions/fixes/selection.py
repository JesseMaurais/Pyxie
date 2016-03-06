import X11 as X
from X11 import bit
from X11.extensions.fixes import Callable

SubType = bit.enum(
	"""
	SetSelectionOwnerNotify
	SelectionWindowDestroyNotify
	SelectionClientCloseNotify
	"""
	)
	
Mask = bit.mask(
	"""
	SetSelectionOwnerNotify
	SelectionWindowDestroyNotify
	SelectionClientCloseNotify
	"""
	)

class SelectionNotify(X.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('subtype', X.CARD),
		('owner', X.Window),
		('selection', X.Atom),
		('timestamp', X.Time),
		('selection_timestamp', X.Time)
		]
		
from X11.event import Event
Event._fields_.append(('xselectionnotify', SelectionNotify))

X.Display.SelectSelectionInput = Callable(
	'XFixesSelectSelectionInput', None,
	['self', X.Display],
	['window', X.Window],
	['selection', X.Atom],
	['mask', X.Bitmask, Mask.every]
	)
	
