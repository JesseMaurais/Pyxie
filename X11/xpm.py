import X11 as X, bit, ctypes

class Extension(ctypes.Structure):
	_fields_ = [
		('name', X.STRING8),
		('nlines', X.INT),
		('lines', X.ArrayOf(X.STRING8))
		]

class ColorSymbol(ctypes.Structure):
	_fields_ = [
		('name', X.STRING8),
		('value', X.STRING8),
		('pixel', X.Pixel)
		]

class Color(ctypes.Structure):
	_fields_ = [
		('string', X.STRING8),
		('symbolic', X.STRING8),
		('m_color', X.STRING8),
		('g4_color', X.STRING8),
		('g_color', X.STRING8),
		('c_color', X.STRING8)
		]

class Image(ctypes.Structure):
	_fields_ = [
		('width', X.INT),
		('height', X.INT),
		('cpp', X.INT),
		('ncolors', X.INT),
		('color_table', X.INT),
		('data', X.STRING8)
		]

class Info(ctypes.Structure):
	_fields_ = [
		('mask', X.Bitmask),
		('hints_comment', X.STRING8),
		('colors_comment', X.STRING8),
		('pixels_comment', X.STRING8),
		('x_hotspot', X.INT),
		('y_hotspot', X.INT),
		('nextensions', X.INT),
		('extensions', X.ArrayOf(Extension))
		]

AllocColorFunc = ctypes.CFUNCTYPE(X.INT, X.Display, X.Colormap, X.String, X.AddressOf(X.Color), X.Pointer)

FreeColorsFunc = ctypes.CFUNCTYPE(X.INT, X.Display, X.Colormap, X.ArrayOf(X.Pixel), X.INT, X.Pointer)

class Attributes(ctypes.Structure):
	_fields_ = [
		('mask', X.CARD),
		('visual', X.Visual),
		('colormap', X.Colormap),
		('depth', X.INT),
		('width', X.INT),
		('height', X.INT),
		('x_hotspot', X.INT),
		('y_hotspot', X.INT),
		('cpp', X.INT),
		('pixels', X.AddressOf(X.Pixel)),
		('npixels', X.INT),
		('colorsymbols', X.ArrayOf(ColorSymbol)),
		('nsymbols', X.INT),
		('rgb_fname', X.STRING8),
		('nextensions', X.INT),
		('extensions', X.ArrayOf(Extension)),
		('ncolors', X.INT),
		('color_table', X.ArrayOf(Color)),
		('hints_comment', X.STRING8),
		('colors_comment', X.STRING8),
		('pixels_comment', X.STRING8),
		('mask_pixel', X.Pixel),
		('exact_colors', X.BOOL),
		('closeness', X.INT),
		('red_closeness', X.INT),
		('green_closeness', X.INT),
		('blue_closeness', X.INT),
		('color_key', X.INT),
		('alloc_pixels', X.ArrayOf(X.Pixel)),
		('nalloc_pixels', X.INT),
		('alloc_close_colors', X.BOOL),
		('bitmap_format', X.CARD),
		('alloc_color', AllocColorFunc),
		('free_colors', FreeColorsFunc),
		('color_closure', X.Pointer)
		]
		
Mask = bit.mask(
	"""
	Visual
	Colormap
	Depth
	Size
	Hotspot
	CharsPerPixel
	ColorSymbols
	RgbFilename
	Infos
	Pixels
	Extensions
	ExactColors
	Closeness
	RgbCloseness
	ColorKey
	ColorTable
	AllocPixels
	AllocCloseColors
	BitmapFormat
	AllocColor
	FreeColors
	ColorClosure
	"""
	)


Callable = X.Wrapper('Xpm')

LibraryVersion = Callable('XpmLibraryVersion')

	
### Pixmap ####################################################
	

X.Display.ReadFileToPixmap = Callable(
	'XpmReadFileToPixmap', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['filename', X.String],
	['return_pixmap', X.Pixmap],
	['return_shape', X.Pixmap],
	['return_attributes', Attributes]
	)

X.Display.WriteFileFromPixmap = Callable(
	'XpmWriteFileFromPixmap', int,
	['self', X.Display],
	['filename', X.String],
	['pixmap', X.Pixmap],
	['shape', X.Pixmap],
	['attributes', X.ByRef(Attributes)]
	)
	
X.Display.ReadPixmapFile = X.Display.ReadFileToPixmap
X.Display.WritePixmapFile = X.Display.WriteFileFromPixmap
	
# Data
	
X.Display.CreatePixmapFromData = Callable(
	'XpmCreatePixmapFromData', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['data', X.ArrayOf(X.String)],
	['return_pixmap', X.Pixmap],
	['return_shape', X.Pixmap],
	['return_attributes', Attributes]
	)
	
X.Display.CreateDataFromPixmap = Callable(
	'XpmCreateDataFromPixmap', int,
	['self', X.Display],
	['return_data', X.ArrayOf(X.STRING8)],
	['pixmap', X.Pixmap],
	['shape', X.Pixmap],
	['attributes', X.ByRef(Attributes)]
	)

# Buffer

X.Display.CreatePixmapFromBuffer = Callable(
	'XpmCreatePixmapFromBuffer', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['buffer', X.String],
	['return_pixmap', X.Pixmap],
	['return_shape', X.Pixmap],
	['return_attributes', X.Pixmap]
	)
	
X.Display.CreateBufferFromPixmap = Callable(
	'XpmCreateBufferFromPixmap', int,
	['self', X.Display],
	['return_buffer', X.String],
	['pixmap', X.Pixmap],
	['shape', X.Pixmap],
	['attributes', X.ByRef(Attributes)]
	)

	
### Image #####################################################


X.Display.ReadFileToImage = Callable(
	'XpmReadFileToImage', int,
	['self', X.Display],
	['filename', X.String],
	['return_image', X.Image],
	['return_shape', X.Image],
	['return_attributes', Attributes]
	)
	
X.Display.WriteFileFromImage = Callable(
	'XpmWriteFileFromImage', int,
	['self', X.Display],
	['filename', X.String],
	['image', X.Image], 
	['shape', X.Image],
	['attributes', X.ByRef(Attributes)]
	)
	
# Data
	
X.Display.CreateImageFromData = Callable(
	'XpmCreateImageFromData', int,
	['self', X.Display],
	['data', X.ArrayOf(X.String)],
	['return_image', X.Image],
	['return_shape', X.Image],
	['return_attributes', Attributes]
	)
	
X.Display.CreateDataFromImage = Callable(
	'XpmCreateDataFromImage', int,
	['self', X.Display],
	['data_return', X.ArrayOf(X.STRING8)],
	['image', X.Image],
	['shape', X.Image],
	['attributes', X.ByRef(Attributes)]
	)
	
# Buffer

X.Display.CreateImageFromBuffer = Callable(
	'XpmCreateImageFromBuffer', int,
	['self', X.Display],
	['buffer', X.String],
	['return_image', X.Pixmap],
	['return_shape', X.Pixmap],
	['return_attributes', X.Pixmap]
	)
	
X.Display.CreateBufferFromImage = Callable(
	'XpmCreateBufferFromImage', int,
	['self', X.Display],
	['buffer_return', X.String],
	['image', X.Image],
	['shape', X.Image],
	['attributes', X.ByRef(Attributes)]
	)

