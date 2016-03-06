import X11 as X, bit, ctypes

class Key(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('root', X.Window),
		('subwindow', X.Window),
		('time', X.Time),
		('x', X.INT),
		('y', X.INT),
		('x_root', X.INT),
		('y_root', X.INT),
		('state', X.CARD),
		('keycode', X.CARD),
		('same_screen', X.BOOL)
		]

class Button(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('root', X.Window),
		('subwindow', X.Window),
		('time', X.Time),
		('x', X.INT),
		('y', X.INT),
		('x_root', X.INT),
		('y_root', X.INT),
		('state', X.CARD),
		('button', X.CARD),
		('same_screen', X.BOOL)
		]

class Motion(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('root', X.Window),
		('subwindow', X.Window),
		('time', X.Time),
		('x', X.INT),
		('y', X.INT),
		('x_root', X.INT),
		('y_root', X.INT),
		('state', X.CARD),
		('is_hint', X.BOOL),
		('same_screen', X.BOOL)
		]

class Crossing(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('root', X.Window),
		('subwindow', X.Window),
		('time', X.Time),
		('x', X.INT),
		('y', X.INT),
		('x_root', X.INT),
		('y_root', X.INT),
		('mode', X.CARD),
		('detail', X.INT),
		('same_screen', X.BOOL),
		('focus', X.BOOL),
		('state', X.CARD)
		]

class FocusChange(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),		
		('window', X.Window),
		('mode', X.INT),
		('detail', X.INT)
		]

class Keymap(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('key_vector', X.KeyCode*32)
		]

class Expose(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('x', X.INT),
		('y', X.INT),
		('width', X.INT),
		('height', X.INT),
		('count', X.INT)
		]

class GraphicsExpose(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('drawable', X.Drawable),
		('x', X.INT),
		('y', X.INT),
		('width', X.INT),
		('height', X.INT),
		('count', X.INT),
		('major_code', X.CARD),
		('minor_code', X.CARD)
		]

class NoExpose(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('drawable', X.Drawable),
		('major_code', X.CARD),
		('minor_code', X.CARD)
		]

VisibilityState = bit.enum('Unobscured PartiallyObscured FullyObscured')

class Visibility(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('state', X.CARD)
		]

class CreateNotify(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('parent', X.Window),
		('window', X.Window),
		('x', X.INT),
		('y', X.INT),
		('width', X.INT),
		('height', X.INT),
		('border_width', X.INT),
		('override_redirect', X.BOOL)
		]

class DestroyNotify(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('event', X.Window),
		('window', X.Window)
		]

class UnmapNotify(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('event', X.Window),
		('window', X.Window),
		('from_configure', X.BOOL)
		]

class MapNotify(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('event', X.Window),
		('window', X.Window),
		('override_redirect', X.BOOL)
		]

class MapRequest(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('parent', X.Window),
		('window', X.Window)
		]

class Reparent(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('event', X.Window),
		('window', X.Window),
		('parent', X.Window),
		('x', X.INT),
		('y', X.INT),
		('override_redirect', X.BOOL)
		]

class Configure(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('event', X.Window),
		('window', X.Window),
		('x', X.INT),
		('y', X.INT),
		('width', X.INT),
		('height', X.INT),
		('border_width', X.INT),
		('above', X.Window),
		('override_redirect', X.BOOL)
		]

class Gravity(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('event', X.Window),
		('window', X.Window),
		('x', X.INT),
		('y', X.INT)
		]

class ResizeRequest(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('width', X.INT),
		('height', X.INT)
		]

class ConfigureRequest(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('parent', X.Window),
		('window', X.Window),
		('x', X.INT),
		('y', X.INT),
		('width', X.INT),
		('height', X.INT),
		('border_width', X.INT),
		('above', X.Window),
		('detail', X.INT),
		('value_mask', X.Bitmask)
		]

class Circulate(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('event', X.Window),
		('window', X.Window),
		('place', X.Integer)
		]

class CirculateRequest(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('parent', X.Window),
		('window', X.Window),
		('place', X.CARD)
		]

PropertyState = bit.enum('NewValue Delete')

class Property(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('selection', X.Atom),
		('time', X.Time),
		('state', X.CARD)
		]

class SelectionClear(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('selection', X.Atom),
		('time', X.Time)
		]

class SelectionRequest(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('requestor', X.Window),
		('selection', X.Atom),
		('target', X.Atom),
		('property', X.Atom),
		('time', X.Time)
		]

class Selection(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('requestor', X.Window),
		('selection', X.Atom),
		('target', X.Atom),
		('property', X.Atom),
		('time', X.Time)
		]

class ColormapNotify(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('colormap', X.Colormap),
		('new', X.BOOL),
		('state', X.CARD)
		]

class ClientData(ctypes.Union):
	_fields_ = [
		('b', X.CARD8*20),
		('s', X.CARD16*10),
		('l', X.CARD32*5)
		]

class ClientMessage(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('message_type', X.Atom),
		('format', X.INT),
		('data', ClientData)
		]

class Mapping(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window),
		('request', X.CARD),
		('first_keycode', X.INT),
		('count', X.INT)
		]

class Any(ctypes.Structure):
	_fields_ = [
		('type', X.CARD),
		('serial', X.INT),
		('send_event', X.BOOL),
		('display', X.Display),
		('window', X.Window)
		]

class Event(ctypes.Union):
	_fields_ = [
		('type', X.INT),
		('xany', Any),
		('xkey', Key),
		('xbutton', Button),
		('xmotion', Motion),
		('xcrossing', Crossing),
		('xfocus', FocusChange),
		('xexpose', Expose),
		('xgraphicsexpose', GraphicsExpose),
		('xnoexpose', NoExpose),
		('xvisibility', Visibility),
		('xcreatewindow', CreateNotify),
		('xdestroywindow', DestroyNotify),
		('xunmap', UnmapNotify),
		('xmap', MapNotify),
		('xmaprequest', MapRequest),
		('xreparent', Reparent),
		('xconfigure', Configure),
		('xgravity', Gravity),
		('xresizerequest', ResizeRequest),
		('xconfigurerequest', ConfigureRequest),
		('xcirculate', Circulate),
		('xcirculaterequest', CirculateRequest),
		('xproperty', Property),
		('xselectionclear', SelectionClear),
		('xselectionrequest', SelectionRequest),
		('xselection', Selection),
		('xcolormap', ColormapNotify),
		('xclient', ClientMessage),
		('xmapping', Mapping),
		('xkeymap', Keymap),
		('pad', X.INT*24)
		]


### Constants #################################################	


Type = bit.enum(
	"""
	Error
	Reply
	KeyPress
	KeyRelease
	ButtonPress
	ButtonRelease
	MotionNotify
	EnterNotify
	LeaveNotify
	FocusIn
	FocusOut
	KeymapNotify
	Expose
	GraphicsExpose
	NoExpose
	VisibilityNotify
	CreateNotify
	DestroyNotify
	UnmapNotify
	MapNotify
	MapRequest
	ReparentNotify
	ConfigureNotify
	ConfigureRequest
	GravityNotify
	ResizeRequest
	CirculateNotify
	CirculateRequest
	PropertyNotify
	SelectionClear
	SelectionRequest
	SelectionNotify
	ColormapNotify
	ClientMessage
	MappingNotify
	Generic
	"""
	)

Mask = bit.mask(
	"""
	KeyPress
	KeyRelease
	ButtonPress
	ButtonRelease
	EnterWindow
	LeaveWindow
	PointerMotion
	PointerMotionHint
	Button1Motion
	Button2Motion
	Button3Motion
	Button4Motion
	Button5Motion
	ButtonMotion
	KeymapState
	Exposure
	VisibilityChange
	StructureNotify
	ResizeRedirect
	SubstructureNotify
	SubstructureRedirect
	FocusChange
	PropertyChange
	ColormapChange
	OwnerGrabButton
	"""
	)


### Methods ###################################################
		

X.Display.NextEvent = X.Callable(
	'XNextEvent', int,
	['self', X.Display],
	['event', X.ByRef(Event)]
	)
	
X.Display.PeekEvent = X.Callable(
	'XPeekEvent', int,
	['self', X.Display],
	['event', X.ByRef(Event)]
	)
	
X.Display.MaskEvent = X.Callable(
	'XMaskEvent', int,
	['self', X.Display],
	['mask', X.Bitmask],
	['event', X.ByRef(Event)]
	)
	
X.Display.WindowEvent = X.Callable(
	'XWindowEvent', int,
	['self', X.Display],
	['window', X.Window],
	['mask', X.Bitmask],
	['event', X.ByRef(Event)]
	)
	
X.Display.CheckTypedEvent = X.Callable(
	'XCheckTypedEvent', bool,
	['self', X.Display],
	['type', X.Cardinal],
	['event', X.ByRef(Event)]
	)
	
X.Display.CheckMaskEvent = X.Callable(
	'XCheckMaskEvent', bool,
	['self', X.Display],
	['mask', X.Bitmask],
	['event', X.ByRef(Event)]
	)
	
X.Display.CheckWindowEvent = X.Callable(
	'XCheckWindowEvent', bool,
	['self', X.Display],
	['window', X.Window],
	['mask', X.Bitmask],
	['event', X.ByRef(Event)]
	)
	
X.Display.CheckTypedWindowEvent = X.Callable(
	'XCheckTypedWindowEvent', bool,
	['self', X.Display],
	['window', X.Window],
	['type', X.Cardinal],
	['event', X.ByRef(Event)]
	)
	
X.Display.SelectInput = X.Callable(
	'XSelectInput', int,
	['self', X.Display],
	['window', X.Window],
	['mask', X.Bitmask, Mask.every]
	)
	
X.Display.SendEvent = X.Callable(
	'XSendEvent', X.Status,
	['self', X.Display],
	['window', X.Window],
	['propogate', X.BOOL, False],
	['mask', X.Bitmask, 0],
	['event', X.ByRef(Event)]
	)
	
X.Display.PutBackEvent = X.Callable(
	'XPutBackEvent', None,
	['self', X.Display],
	['event', X.ByRef(Event)]
	)
	
AllowMode = bit.enum(
	"""
	AsyncPointer
	SyncPointer
	ReplayPointer
	AsyncKeyboard
	SyncKeyboard
	ReplayKeyboard
	AsyncBoth
	AyncBoth
	"""
	)
	
X.Display.AllowEvents = X.Callable(
	'XAllowEvents', int,
	['self', X.Display],
	['mode', X.Cardinal],
	['time', X.Time]
	)
	
Queued = bit.enum('Already AfterFlush AfterReading')
	
X.Display.EventsQueued = X.Callable(
	'XEventsQueued', int,
	['self', X.Display],
	['mode', X.Cardinal, Queued.Already]
	)

X.Display.RebindKeysym = X.Callable(
	'XRebindKeysym', int,
	['self', X.Display],
	['keysym', X.KeySym],
	['mods', X.ListOf(X.KeySym)],
	['n_mods', X.Integer],
	['string', X.String],
	['strlen', X.Integer]
	)
	
class TimeCoord(ctypes.Structure):
	_fields_ = [
		('time', X.Time),
		('x', X.INT16),
		('y', X.INT16)
		]
	
X.Display.GetMotionEvents = X.Callable(
	'XGetMotionEvents', X.ArrayOf(TimeCoord),
	['self', X.Display],
	['window', X.Window],
	['start', X.Time],
	['stop', X.Time],
	['count', X.ByRef(X.INT)]
	)

Event.Filter = X.Callable(
	'XFilterEvent', bool,
	['self', X.ByRef(Event)],
	['window', X.Window]
	)

Key.LookupKeysym = X.Callable(
	'XLookupKeysym', int,
	['self', X.ByRef(Key)],
	['index', X.Integer, 0]
	)

Key.sym = property(Key.LookupKeysym)

Mapping.RefreshKeyboardMapping = X.Callable(
	'XRefreshKeyboardMapping', int,
	['self', X.ByRef(Mapping)]
	)
	
Predicate = ctypes.CFUNCTYPE(X.BOOL, X.Display, ctypes.POINTER(Event), X.Pointer)
	
X.Display.IfEvent = X.Callable(
	'XIfEvent', int,
	['self', X.Display],
	['return', Event],
	['predicate', Predicate],
	['arg', X.Pointer, None]
	)
	
X.Display.PeekIfEvent = X.Callable(
	'XPeekIfEvent', int,
	['self', X.Display],
	['return', Event],
	['predicate', Predicate],
	['arg', X.Pointer, None]
	)

X.Display.CheckIfEvent = X.Callable(
	'XCheckIfEvent', bool,
	['self', X.Display],
	['return', Event],
	['predicate', Predicate],
	['arg', X.Pointer, None]
	)	


X.Display.pending = X.extern_property('XPending')

	
### Sugar #####################################################
	

def Pending(display):
	event = Event()
	while display.pending:
		display.NextEvent(event)
		yield event
	
X.Display.events = property(Pending)
		
def Next(display):
	event = Event()
	display.NextEvent(event)
	return event

X.Display.__iter__ = lambda self: self

X.Display.next = Next

