import X11 as X, bit, ctypes


Format = bit.enum('XYBitmap XYPixmap ZPixmap')

class ImageStruct(ctypes.Structure):
	'Pull information about an image format'
	
	_fields_ = [
		('width', X.INT),
		('height', X.INT),
		('xoffset', X.INT),
		('format', X.CARD),
		('data', X.ArrayOf(X.BYTE)),
		('byte_order', X.CARD),
		('bitmap_unit', X.INT),
		('bitmap_bit_order', X.INT),
		('bitmap_pad', X.INT),
		('depth', X.INT),
		('bytes_per_line', X.INT),
		('bits_per_pixel', X.INT),
		('red_mask', X.Bitmask),
		('green_mask', X.Bitmask),
		('blue_mask', X.Bitmask)
		]
		
	def __init__(self, image):
		from ctypes import memmove, sizeof
		memmove(self, image, sizeof(self))

#InitImage = X.Callable(
#	'XInitImage', X.Status,
#	['image', X.Image]
#	)

X.Display.CreateImage = X.Callable(
	'XCreateImage', X.Image,
	['self', X.Display],
	['visual', X.Visual],
	['depth', X.Integer, 24],
	['format', X.Integer, Format.XYPixmap],
	['offset', X.Integer, 0],
	['data', X.String],
	['width', X.Integer],
	['height', X.Integer],
	['bitmap_pad', X.Integer, 32],
	['bytes_per_line', X.Integer]
	)
	
X.Image.Destroy = X.Callable(
	'XDestroyImage', int,
	['self', X.Image]
	)

X.Display.PutImage = X.Callable(
	'XPutImage', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['image', X.Image],
	['src_x', X.Integer, 0],
	['src_y', X.Integer, 0],
	['dst_x', X.Integer, 0],
	['dst_y', X.Integer, 0],
	['width', X.Integer],
	['height', X.Integer]
	)

X.Display.GetImage = X.Callable(
	'XGetImage', X.Image,
	['self', X.Display],
	['drawable', X.Drawable],
	['x', X.Integer, 0],
	['y', X.Integer, 0],
	['width', X.Integer],
	['height', X.Integer],
	['plane_mask', X.Bitmask, -1],
	['format', X.Integer, Format.XYPixmap]
	)

X.Display.GetSubImage = X.Callable(
	'XGetSubImage', X.Image,
	['self', X.Display],
	['drawable', X.Drawable],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer],
	['plane_mask', X.Bitmask],
	['format', X.Integer],
	['image', X.Image],
	['dst_x', X.Integer],
	['dst_y', X.Integer]
	)

X.Image.PutPixel = X.Callable(
	'XPutPixel', int,
	['self', X.Image],
	['x', X.Integer],
	['y', X.Integer],
	['pixel', X.Pixel]
	)
	
X.Image.GetPixel = X.Callable(
	'XGetPixel', X.Pixel,
	['self', X.Image],
	['x', X.Integer],
	['y', X.Integer]
	)
	
X.Image.AddPixel = X.Callable(
	'XAddPixel', int,
	['self', X.Image],
	['value', X.Pixel]
	)
	
X.Image.SubImage = X.Callable(
	'XSubImage', X.Image,
	['self', X.Image],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer]
	)

