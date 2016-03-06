import X11 as X, bit

XA = bit.enum(
	"""
	ANY
	PRIMARY
	SECONDARY
	ARC
	ATOM
	BITMAP
	CARDINAL
	COLORMAP
	CURSOR
	CUT_BUFFER0
	CUT_BUFFER1
	CUT_BUFFER2
	CUT_BUFFER3
	CUT_BUFFER4
	CUT_BUFFER5
	CUT_BUFFER6
	CUT_BUFFER7
	DRAWABLE
	FONT
	INTEGER
	PIXMAP
	POINT
	RECTANGLE
	RESOURCE_MANAGER
	RGB_COLOR_MAP
	RGB_BEST_MAP
	RGB_BLUE_MAP
	RGB_DEFAULT_MAP
	RGB_GRAY_MAP
	RGB_GREEN_MAP
	RGB_RED_MAP
	STRING
	VISUALID
	WINDOW
	WM_COMMAND
	WM_HINTS
	WM_CLIENT_MACHINE
	WM_ICON_NAME
	WM_ICON_SIZE
	WM_NAME
	WM_NORMAL_HINTS
	WM_SIZE_HINTS
	WM_ZOOM_HINTS
	MIN_SPACE
	NORM_SPACE
	MAX_SPACE
	END_SPACE
	SUPERSCRIPT_X
	SUPERSCRIPT_Y
	SUBSCRIPT_X
	SUBSCRIPT_Y
	UNDERLINE_POSITION
	UNDERLINE_THICKNESS
	STRIKEOUT_ASCENT
	STRIKEOUT_DESCENT
	ITALIC_ANGLE
	X_HEIGHT
	QUAD_WIDTH
	WEIGHT
	POINT_SIZE
	RESOLUTION
	COPYRIGHT
	NOTICE
	FONT_NAME
	FAMILY_NAME
	FULL_NAME
	CAP_HEIGHT
	WM_CLASS
	WM_TRANSIENT_FOR
	"""
	)


### Atom Queries ##############################################


X.Display.InternAtom = X.Callable(
	'XInternAtom', X.Atom,
	['self', X.Display],
	['name', X.String],
	['only_if_exists', X.BOOL, False]
	)

X.Display.InternAtoms = X.Callable(
	'XInternAtoms', X.Status,
	['self', X.Display],
	['names', X.ListOf(X.String)],
	['count', X.Integer],
	['only_if_exists', X.BOOL, False],
	['atoms_out', X.AddressOf(X.Atom)]
	)

X.Display.GetAtomName = X.Callable(
	'XGetAtomName', X.STRING8,
	['self', X.Display],
	['atom', X.Atom]
	)

X.Display.GetAtomNames = X.Callable(
	'XGetAtomNames', X.Status,
	['self', X.Display],
	['atoms', X.ListOf(X.Atom)],
	['natoms', X.Integer],
	['names_out', X.AddressOf(X.String)]
	)


### Window Properties #########################################


X.Display.GetWindowProperty = X.Callable(
	'XGetWindowProperty', int,
	['self', X.Display],
	['window', X.Window],
	['property', X.Atom],
	['long_offset', X.Integer, 0],
	['long_length', X.Integer, 1],
	['delete', X.BOOL, False],
	['type', X.Atom, XA.STRING],
	['return_actual_type', X.Atom],
	['return_actual_format', X.INT],
	['return_items', X.INT],
	['return_bytes_after', X.INT],
	['return_property', X.Pointer]
	)
	
PropertyMode = bit.enum('Replace Prepend Append')

X.Display.ChangeProperty = X.Callable(
	'XChangeProperty', int,
	['self', X.Display],
	['window', X.Window],
	['property', X.Atom],
	['type', X.Atom, XA.STRING],
	['format', X.Integer, 8],
	['mode', X.Cardinal, PropertyMode.Replace],
	['data', X.Pointer],
	['items', X.Integer]
	)
	
X.Display.DeleteProperty = X.Callable(
	'XDeleteProperty', int,
	['self', X.Display],
	['window', X.Window],
	['property', X.Atom]
	)
	
X.Display.ListProperties = X.Callable(
	'XListProperties', X.ArrayOf(X.Atom),
	['self', X.Display],
	['window', X.Window],
	['count', X.ByRef(X.INT)]
	)
	
def PropertiesList(window):
	n = X.INT()
	props = window.ListProperties(n)
	for i in range(n.value):
		yield props[i]
	X.Free(props)

X.Window.properties = property(PropertiesList)

X.Display.RotateWindowProperties = X.Callable(
	'XRotateWindowProperties', int,
	['self', X.Display],
	['window', X.Window],
	['properties', X.ListOf(X.Atom)],
	['nproperties', X.Integer],
	['npositions', X.Integer]
	)


### Sugar #####################################################


PropertyType = {
	XA.ARC : X.Arc,
	XA.ATOM : X.Atom,
	XA.CARDINAL : X.Cardinal,
	XA.COLORMAP : X.Colormap,
	XA.CURSOR : X.Cursor,
	XA.DRAWABLE : X.Drawable,
	XA.FONT : X.Font,
	XA.INTEGER : X.Integer,
	XA.PIXMAP : X.Pixmap,
	XA.POINT : X.Point,
	XA.RECTANGLE : X.Rectangle,
	XA.STRING : X.String,
	XA.VISUALID : X.VisualID,
	XA.WINDOW : X.Window
	}


X.Atom.atom = XA.ATOM
X.Atom.items = 1
X.Atom.format = 32

X.Drawable.atom = XA.DRAWABLE
X.Drawable.items = 1
X.Drawable.format = 32

X.Window.atom = XA.WINDOW
X.Window.items = 1
X.Window.format = 32

X.Pixmap.atom = XA.PIXMAP
X.Pixmap.items = 1
X.Pixmap.format = 32

X.Font.atom = XA.FONT
X.Font.items = 1
X.Font.format = 32

X.Colormap.atom = XA.COLORMAP
X.Colormap.items = 1
X.Colormap.format = 32

X.VisualID.atom = XA.VISUALID
X.VisualID.items = 1
X.VisualID.format = 32

X.Cursor.atom = XA.CURSOR
X.Cursor.items = 1
X.Cursor.format = 32

X.Cardinal.atom = XA.CARDINAL
X.Cardinal.items = 1
X.Cardinal.format = 32

X.Integer.atom = XA.INTEGER
X.Integer.items = 1
X.Integer.format = 32

X.String.atom = XA.STRING
X.String.items = None
X.String.format = 8

X.Point.atom = XA.POINT
X.Point.items = 2
X.Point.format = 16

X.Rectangle.atom = XA.RECTANGLE
X.Rectangle.items = 4
X.Rectangle.format = 16

X.Arc.atom = XA.ARC
X.Arc.items = 6
X.Arc.format = 16



def InternAtom(display, name):
	'Assume unknown display attributes are atom names'
	
	atom = display.InternAtom(name, only_if_exists=True).value
	
	if not atom: raise AttributeError, name
		
	# So we don't get called again
	setattr(display, name, atom)
	
	return atom

X.Display.__getattr__ = InternAtom



def GetProperty(window, property, type=XA.ANY, delete=False):
	'Auto convert GetWindowProperty result to its type'

	format = 32
	items = 1
	length = 1
	bytes = None
	data = None

	while length:
		type, format, items, length, bytes = window.GetWindowProperty(
			property, 0, length, delete, type
			)
			
	if type.value in PropertyType:
		data = PropertyType[type.value]()
	else:
		if format == 32:
			data = (X.CARD32 * nitems)()
		if format == 16:
			data = (X.CARD16 * nitems)()
		if format ==  8:
			data = (X.CARD8  * nitems)()

	from ctypes import sizeof, addressof, memmove
	memmove(addressof(data), addressof(bytes), sizeof(data))

	return data



def SetProperty(window, property, data, mode=PropertyMode.Replace):
	'Simpler version of ChangeProperty using class attributes'

	items = data.items or len(data.value)
	
	from ctypes import addressof
	address = addressof(data)

	return window.ChangeProperty(
		property, data.atom, data.format, mode, address, items
		)


def WindowProperty(atom):
	def getprop(window):
		return GetProperty(window, atom)
	def setprop(window, data):
		SetProperty(window, atom, data)
	def delprop(window):
		window.DeleteProperty(atom)	
	return property(getprop, setprop, delprop)


X.Window.Property = staticmethod(WindowProperty)

X.Atom.name = property(lambda atom: atom.GetAtomName())

