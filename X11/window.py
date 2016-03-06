import X11 as X, ctypes, bit

# Use for GetWindowAttributes

class Attributes(ctypes.Structure):
	_fields_ = [
		('x', X.INT),
		('y', X.INT),
		('width', X.INT),
		('height', X.INT),
		('border_width', X.INT),
		('depth', X.INT),
		('visual', X.Visual),
		('root', X.Window),
		('cclass', X.CARD),
		('bit_gravity', X.CARD),
		('win_gravity', X.CARD),
		('backing_store', X.CARD),
		('backing_planes', X.Bitmask),
		('backing_pixel', X.Pixel),
		('save_under', X.BOOL),
		('colormap', X.Colormap),
		('map_installed', X.BOOL),
		('map_state', X.CARD),
		('all_event_masks', X.Bitmask),
		('your_event_mask', X.Bitmask),
		('do_not_propagage_mask', X.Bitmask),
		('override_redirect', X.BOOL),
		('screen', X.Screen)
		]
		
# Use for CreateWindow & ChangeWindowAttributes

class NewAttributes(ctypes.Structure):
	_fields_ = [
		('background_pixmap', X.Pixmap),
		('background_pixel', X.Pixel),
		('border_pixmap', X.Pixmap),
		('border_pixel', X.Pixel),
		('bit_gravity', X.CARD),
		('win_gravity', X.CARD),
		('backing_store', X.CARD),
		('backing_planes', X.Bitmask),
		('backing_pixel', X.Pixel),
		('save_under', X.BOOL),
		('event_mask', X.Bitmask),
		('do_not_propagate_mask', X.Bitmask),
		('override_redirect', X.BOOL),
		('colormap', X.Colormap)
		]

Mask = bit.mask(
	"""
	BackPixmap
	BackPixel
	BorderPixmap
	BorderPixel
	BitGravity
	WinGravity
	BackingStore
	BackingPlanes
	BackingPixel
	OverrideRedirect
	SaveUnder
	EventMask
	DontPropagate
	Colormap
	Cursor
	"""
	)

def MaskAttributes(**args):
	typemap = {
		'background_pixmap':Mask.BackPixmap,
		'background_pixel':Mask.BackPixel,
		'border_pixmap':Mask.BorderPixmap,
		'border_pixel':Mask.BorderPixel,
		'bit_gravity':Mask.BitGravity,
		'win_gravity':Mask.WinGravity,
		'backing_store':Mask.BackingStore,
		'backing_planes':Mask.BackingPlanes,
		'backing_pixel':Mask.BackingPixel,
		'save_under':Mask.SaveUnder,
		'event_mask':Mask.EventMask,
		'do_not_propagate_mask':Mask.DontPropagate,
		'override_redirect':Mask.OverrideRedirect,
		'colormap':Mask.Colormap
		}
	mask = 0
	for key in args:
		mask |= typemap[key]
	return mask, NewAttributes(**args)

# Use for ConfigureWindow & ReconfigureWMWindow

class Changes(ctypes.Structure):
	_fields_ = [
		('x', X.INT),
		('y', X.INT),
		('width', X.INT),
		('height', X.INT),
		('border_width', X.INT),
		('sibling', X.Window),
		('stack_mode', X.CARD)
		]

CW = bit.mask(
	"""
	X
	Y
	Width
	Height
	BorderWidth
	Sibling
	StackMode
	"""
	)

def MaskChanges(**args):
	typemap = {
		'x':CW.X,
		'y':CW.Y,
		'width':CW.Width,
		'height':CW.Height,
		'border_width':CW.BorderWidth,
		'sibling':CW.Sibling,
		'stack_mode':CW.StackMode
		}
	mask = 0
	for key in args:
		mask |= typemap[key]
	return mask, Changes(**args)


### Constants #################################################


Class = bit.enum(
	"""
	CopyFromParent
	InputOutput
	InputOnly
	"""
	)

Gravity = bit.enum(
	"""
	Forget
	NorthWest
	North
	NorthEast
	West
	Center
	East
	SouthWest
	South
	SouthEast
	Static
	"""
	)

BackingStore = bit.enum(
	"""
	NotUseful
	WhenMapped
	Always
	"""
	)

Circulate = bit.enum(
	"""
	RaiseLowest
	LowerHighest
	"""
	)


### Methods ###################################################


X.Display.CreateWindow = X.Callable(
	'XCreateWindow', X.Window,
	['self', X.Display],
	['parent', X.Window],
	['x', X.Integer, -1],
	['y', X.Integer, -1],
	['width', X.Integer, 320],
	['height', X.Integer, 200],
	['border_width', X.Integer, 1],
	['depth', X.Integer, 0],
	['cclass', X.Cardinal, Class.CopyFromParent],
	['visual', X.Visual, X.CopyFromParent],
	['mask', X.Bitmask, 0],
	['new_attributes', X.AddressOf(NewAttributes), None]
	)

X.Display.CreateSimpleWindow = X.Callable(
	'XCreateSimpleWindow', X.Window,
	['self', X.Display],
	['parent', X.Window],
	['x', X.Integer, -1],
	['y', X.Integer, -1],
	['width', X.Integer, 320],
	['height', X.Integer, 200],
	['border_width', X.Integer, 0],
	['border', X.Pixel, 0],
	['background', X.Pixel, 0]
	)
	
X.Display.ChangeWindowAttributes = X.Callable(
	'XChangeWindowAttributes', int,
	['self', X.Display],
	['window', X.Window],
	['mask', X.Bitmask],
	['new_attributes', X.ByRef(NewAttributes)]
	)
	
X.Display.GetWindowAttributes = X.Callable(
	'XGetWindowAttributes', X.Status,
	['self', X.Display],
	['window', X.Window],
	['return', Attributes]
	)
	
X.Display.DestroyWindow = X.Callable(
	'XDestroyWindow', int,
	['self', X.Display],
	['window', X.Window]
	)
		
X.Display.DestroySubwindows = X.Callable(
	'XDestroySubwindows', int,
	['self', X.Display],
	['window', X.Window]
	)

X.Display.MapWindow = X.Callable(
	'XMapWindow', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.UnmapWindow = X.Callable(
	'XUnmapWindow', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.MapSubwindows = X.Callable(
	'XMapSubwindows', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.UnmapSubwindows = X.Callable(
	'XUnmapSubwindows', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.ClearArea = X.Callable(
	'XClearArea', int,
	['self', X.Display],
	['window', X.Window],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer],
	['exposures', X.BOOL, True]
	)
	
X.Display.ClearWindow = X.Callable(
	'XClearWindow', int,
	['self', X.Display],
	['window', X.Window]
	)

X.Display.IconifyWindow = X.Callable(
	'XIconifyWindow', X.Status,
	['self', X.Display],
	['window', X.Window],
	['screen', X.Integer, 0]
	)

X.Display.WithdrawWindow = X.Callable(
	'XWithdrawWindow', X.Status,
	['self', X.Display],
	['window', X.Window],
	['screen', X.Integer, 0]
	)
	
X.Display.ReconfigureWMWindow = X.Callable(
	'XReconfigureWMWindow', X.Status,
	['self', X.Display],
	['window', X.Window],
	['screen', X.Integer],
	['mask', X.Bitmask],
	['changes', X.ByRef(Changes)]
	)
	
	
### Configure #################################################
	

X.Display.ConfigureWindow = X.Callable(
	'XConfigureWindow', int,
	['self', X.Display],
	['window', X.Window],
	['mask', X.Bitmask],
	['changes', X.ByRef(Changes)]
	)

X.Display.MoveWindow = X.Callable(
	'XMoveWindow', int,
	['self', X.Display],
	['window', X.Window],
	['x', X.Integer],
	['y', X.Integer]
	)
	
X.Display.ResizeWindow = X.Callable(
	'XResizeWindow', int,
	['self', X.Display],
	['window', X.Window],
	['width', X.Integer],
	['height', X.Integer]
	)
	
X.Display.MoveResizeWindow = X.Callable(
	'XMoveResizeWindow', int,
	['self', X.Display],
	['window', X.Window],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer]
	)
	
	
### Stack #####################################################
	

X.Display.QueryTree = X.Callable(
	'XQueryTree', X.Status,
	['self', X.Display],
	['window', X.Window],
	['return_root', X.Window],
	['return_parent', X.Window],
	['return_children', X.ArrayOf(X.Window)],
	['return_nchildren', X.INT]
	)

X.Display.ReparentWindow = X.Callable(
	'XReparentWindow', int,
	['self', X.Display],
	['window', X.Window],
	['parent', X.Window],
	['x', X.Integer],
	['y', X.Integer]
	)
	
X.Display.MapRaised = X.Callable(
	'XMapRaised', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.RaiseWindow = X.Callable(
	'XRaiseWindow', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.LowerWindow = X.Callable(
	'XLowerWindow', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.RestackWindows = X.Callable(
	'XRestackWindows', int,
	['self', X.Display],
	['windows', X.ListOf(X.Window)],
	['nwindows', X.Integer]
	)
	
X.Display.CirculateSubwindows = X.Callable(
	'XCirculateSubwindows', int,
	['self', X.Display],
	['window', X.Window],
	['direction', X.Integer]
	)
	
X.Display.CirculateSubwindowsUp = X.Callable(
	'XCirculateSubwindowsUp', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.CirculateSubwindowsDown = X.Callable(
	'XCirculateSubwindowsDown', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.TranslateCoordinates = X.Callable(
	'XTranslateCoordinates', bool,
	['self', X.Display],
	['src', X.Window],
	['dst', X.Window],
	['x', X.Integer],
	['y', X.Integer],
	['return_x', X.INT],
	['return_y', X.INT],
	['return_child', X.Window]
	)


### Attributes ################################################


X.Display.SetWindowBackground = X.Callable(
	'XSetWindowBackground', int,
	['self', X.Display],
	['window', X.Window],
	['background', X.Pixel]
	)
	
X.Display.SetWindowBackgroundPixmap = X.Callable(
	'XSetWindowBackgroundPixmap', int,
	['self', X.Display],
	['window', X.Window],
	['background', X.Pixmap]
	)
	
X.Display.SetWindowBorder = X.Callable(
	'XSetWindowBorder', int,
	['self', X.Display],
	['window', X.Window],
	['border', X.Pixel]
	)
	
X.Display.SetWindowBorderPixmap = X.Callable(
	'XSetWindowBorderPixmap', int,
	['self', X.Display],
	['window', X.Window],
	['border', X.Pixmap]
	)

X.Display.SetWindowBorderWidth = X.Callable(
	'XSetWindowBorderWidth', int,
	['self', X.Display],
	['window', X.Window],
	['width', X.Integer]
	)
	
X.Display.SetWindowColormap = X.Callable(
	'XSetWindowColormap', int,
	['self', X.Display],
	['window', X.Window],
	['colormap', X.Colormap]
	)


