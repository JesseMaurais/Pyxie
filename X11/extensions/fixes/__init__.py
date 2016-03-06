import X11 as X
from X11 import bit

__all__ = [
	'cursor',
	'region',
	'saveset',
	'selection'
	]

Callable = X.Wrapper('Xfixes')

X.Display.QueryFixesExtension = Callable(
	'XFixesQueryExtension', bool,
	['self', X.Display],
	['return_event', X.CARD],
	['return_error', X.CARD]
	)
	
X.Display.QueryFixesVersion = Callable(
	'XFixesQueryVersion', X.Status,
	['self', X.Display],
	['return_major', X.INT],
	['return_minor', X.INT]
	)
	
Notify = bit.enum(
	"""
	Selection
	Cursor
	"""
	)
