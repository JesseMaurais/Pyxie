import X11 as X, bit, ctypes
import event

Status = bit.enum(
	"""
	Success
	BadRequest
	BadValue
	BadWindow
	BadPixmap
	BadAtom
	BadCursor
	BadFont
	BadMatch
	BadDrawable
	BadAccess
	BadAlloc
	BadColor
	BadGC
	BadIDChoice
	BadName
	BadLength
	BadImplementation
	"""
	)

X.Display.GetErrorText = X.Callable(
	'XGetErrorText', int,
	['self', X.Display],
	['code', X.Cardinal],
	['buffer', X.String],
	['length', X.Integer]
	)
	
X.Display.GetErrorDatabaseText = X.Callable(
	'XGetErrorDatabaseText', int,
	['self', X.Display],
	['name', X.String],
	['message', X.String],
	['default', X.String],
	['buffer', X.String],
	['length', X.Integer]
	)

DisplayName = X.Callable(
	'XDisplayName', X.STRING8,
	['string', X.String]
	)

Handler = ctypes.CFUNCTYPE(X.INT, X.Display, ctypes.POINTER(event.Error))

SetHandler = X.Callable(
	'XSetErrorHandler', int,
	['handler', Handler]
	)
	
IOHandler = ctypes.CFUNCTYPE(X.INT, X.Display)
	
SetIOHandler = X.Callable(
	'XSetIOErrorHandler', int,
	['iohandler', IOHandler]
	)
