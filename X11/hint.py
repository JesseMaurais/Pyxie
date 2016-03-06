import X11 as X, bit, ctypes
from text import TextProperty
from atom import XA


class SizeHints(ctypes.Structure):
	_fields_ = [
		('flags', X.Bitmask),
		('x', X.INT),
		('y', X.INT),
		('width', X.INT),
		('height', X.INT),
		('min_width', X.INT),
		('min_height', X.INT),
		('max_width', X.INT),
		('max_height', X.INT),
		('inc_width', X.INT),
		('inc_height', X.INT),
		('min_aspect_x', X.INT),
		('min_aspect_y', X.INT),
		('max_aspect_x', X.INT),
		('max_aspect_y', X.INT),
		('base_width', X.INT),
		('base_height', X.INT),
		('win_gravity', X.CARD)
		]
		
	atom = XA.WM_SIZE_HINTS
	format = 32
	nitems = len(_fields_)

SizeFlags = bit.mask(
	"""
	USPosition
	USSize
	PPosition
	PSize
	PMinSize
	PMaxSize
	PResizeInc
	PAspect
	PBaseSize
	PWinGravity
	"""
	)

def Size(**args):
	typemap = {
		'x':SizeFlags.PPosition,
		'width':SizeFlags.PSize,
		'min_width':SizeFlags.PMinSize,
		'max_width':SizeFlags.PMaxSize,
		'inc_width':SizeFlags.PResizeInc,
		'min_aspect_x':SizeFlags.PAspect,
		'base_width':SizeFlags.PBaseSize,
		'win_gravity':SizeFlags.PWinGravity
		}
	mask = 0
	for key in args:
		if key in typemap:
			mask |= typemap[key]
	return SizeHints(flags=mask, **args)

X.Display.GetSizeHints = X.Callable(
	'XGetSizeHints', X.Status,
	['self', X.Display],
	['window', X.Window],
	['return_hints', SizeHints],
	['property', X.Atom]
	)
	
X.Display.SetSizeHints = X.Callable(
	'XSetSizeHints', None,
	['self', X.Display],
	['window', X.Window],
	['hints', X.AddressOf(SizeHints)],
	['property', X.Atom]
	)

X.Display.GetWMSizeHints = X.Callable(
	'XGetWMSizeHints', X.Status,
	['self', X.Display],
	['window', X.Window],
	['hints_return', SizeHints],
	['supplied_return', X.INT],
	['property', X.Atom]
	)

X.Display.SetWMSizeHints = X.Callable(
	'XSetWMSizeHints', None,
	['self', X.Display],
	['window', X.Window],
	['hints', X.ByRef(SizeHints)],
	['property', X.Atom]
	)
	
X.Display.GetNormalHints = X.Callable(
	'XGetNormalHints', X.Status,
	['self', X.Display],
	['window', X.Window],
	['hints_return', SizeHints]
	)
	
X.Display.SetNormalHints = X.Callable(
	'XSetNormalHints', X.Status,
	['self', X.Display],
	['window', X.Window],
	['hints', X.ByRef(SizeHints)]
	)

X.Display.GetWMNormalHints = X.Callable(
	'XGetWMNormalHints', X.Status,
	['self', X.Display],
	['window', X.Window],
	['hints_return', SizeHints],
	['supplied_return', X.INT]
	)
	
X.Display.SetWMNormalHints = X.Callable(
	'XSetWMNormalHints', X.Status,
	['self', X.Display],
	['window', X.Window],
	['hints', X.AddressOf(SizeHints)]
	)

X.Display.GetZoomHints = X.Callable(
	'XGetZoomHints', X.Status,
	['self', X.Display],
	['window', X.Window],
	['hints_return', SizeHints]
	)
	
X.Display.SetZoomHints = X.Callable(
	'XSetZoomHints', int,
	['self', X.Display],
	['window', X.Window],
	['hints', X.ByRef(SizeHints)]
	)
	
X.Display.SetStandardProperties = X.Callable(
	'XSetStandardProperties', int,
	['self', X.Display],
	['window', X.Window],
	['window_name', X.String],
	['icon_name', X.String],
	['icon_pixmap', X.Pixmap],
	['argv', X.ListOf(X.String)],
	['argc', X.Integer],
	['hints', X.AddressOf(SizeHints)]
	)
	
X.Display.WMGeometry = X.Callable(
	'XWMGeometry', int,
	['self', X.Display],
	['screen', X.Integer],
	['user_geom', X.String],
	['default_geom', X.String],
	['border_width', X.Integer],
	['hints', X.ByRef(SizeHints)],
	['x_return', X.INT],
	['y_return', X.INT],
	['width_return', X.INT],
	['height_return', X.INT],
	['gravity_return', X.CARD]
	)
	


class IconSize(ctypes.Structure):
	_fields_ = [
		('min_width', X.INT),
		('min_height', X.INT),
		('max_width', X.INT),
		('max_height', X.INT),
		('inc_width', X.INT),
		('inc_height', X.INT)
		]

X.Display.SetIconSizes = X.Callable(
	'XSetIconSizes', int,
	['self', X.Display],
	['window', X.Window],
	['sizes', X.ListOf(IconSize)],
	['nsizes', X.Integer]
	)
	
X.Display.GetIconSizes = X.Callable(
	'XGetIconSizes', X.Status,
	['self', X.Display],
	['window', X.Window],
	['sizes_return', X.ArrayOf(IconSize)],
	['nsizes_return', X.INT32]
	)
	


class ClassHint(ctypes.Structure):
	_fields_ = [
		('res_name', X.STRING8),
		('res_class', X.STRING8)
		]

X.Display.SetClassHint = X.Callable(
	'XSetClassHint', None,
	['self', X.Display],
	['window', X.Window],
	['hint', X.ByRef(ClassHint)]
	)
	
X.Display.GetClassHint = X.Callable(
	'XGetClassHint', X.Status,
	['self', X.Display],
	['window', X.Window],
	['hint_return', ClassHint]
	)



class WindowManagerHints(ctypes.Structure):
	_fields_ = [
		('flags', X.Bitmask),
		('wminput', X.BOOL),
		('initial_state', X.CARD),
		('icon_pixmap', X.Pixmap),
		('icon_window', X.Window),
		('icon_x', X.INT),
		('icon_y', X.INT),
		('icon_mask', X.Pixmap),
		('window_group', X.ID)
		]

WMFlags = bit.mask(
	"""
	Input
	State
	IconPixmap
	IconWindow
	IconPosition
	IconMask
	WindowGroup
	UNUSED
	Urgency
	"""
	)
	
WMInitialState = bit.enum(
	"""
	Withdrawn
	Normal
	Zoom
	Iconic
	Inactive
	"""
	)

def WindowManager(**args):
	typemap = {
		'wminput':WMFlags.Input,
		'initial_state':WMFlags.State,
		'icon_pixmap':WMFlags.IconPixmap,
		'icon_window':WMFlags.IconWindow,
		'icon_x':WMFlags.IconPosition,
		'icon_y':WMFlags.IconPosition,
		'icon_mask':WMFlags.IconMask,
		'window_group':WMFlags.WindowGroup
		}
	mask = 0
	for key in args:
		if key == 'urgent':
			mask |= WMFlags.Urgency
		else:
			mask |= typemap[key]
			
	return WindowManagerHints(flags=mask, **args)
		
X.Display.SetWMHints = X.Callable(
	'XSetWMHints', int,
	['self', X.Display],
	['window', X.Window],
	['hint', X.ByRef(WindowManagerHints)]
	)
		
X.Display.GetWMHints = X.Callable(
	'XGetWMHints', X.AddressOf(WindowManagerHints),
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.SetWMClientMachine = X.Callable(
	'XSetWMClientMachine', None,
	['self', X.Display],
	['window', X.Window],
	['text', X.ByRef(TextProperty)]
	)
	
X.Display.GetWMClientMachine = X.Callable(
	'XGetWMClientMachine', X.Status,
	['self', X.Display],
	['window', X.Window],
	['text_return', TextProperty]
	)
	
X.Display.SetWMName = X.Callable(
	'XSetWMName', None,
	['self', X.Display],
	['window', X.Window],
	['text_return', TextProperty]
	)
	
X.Display.GetWMName = X.Callable(
	'XGetWMName', X.Status,
	['self', X.Display],
	['window', X.Window],
	['text', X.ByRef(TextProperty)]
	)
	
X.Display.SetWMIconName = X.Callable(
	'XSetWMIconName', None,
	['self', X.Display],
	['window', X.Window],
	['text', X.ByRef(TextProperty)]
	)
	
X.Display.GetWMIconName = X.Callable(
	'XGetWMIconName', X.Status,
	['self', X.Display],
	['window', X.Window],
	['text_return', TextProperty]
	)
	
X.Display.SetWMProperties = X.Callable(
	'XSetWMProperties', None,
	['self', X.Display],
	['window', X.Window],
	['window_name', X.ByRef(TextProperty)],
	['icon_name', X.ByRef(TextProperty)],
	['argv', X.ArrayOf(X.String)],
	['argc', X.Integer],
	['normal_hints', X.ByRef(SizeHints)],
	['wm_hints', X.ByRef(WindowManagerHints)],
	['class_hints', X.ByRef(ClassHint)]
	)

