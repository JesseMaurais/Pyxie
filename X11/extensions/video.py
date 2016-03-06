import X11 as X, ctypes
from X11 import bit


class Port(X.ID):
	pass
class Encoding(X.ID):
	pass


class Attribute(ctypes.Structure):
	_fields_ = [
		('flags', X.INT),
		('min_value', X.INT),
		('max_value', X.INT),
		('name', X.STRING8)
		]

class Format(ctypes.Structure):
	_fields_ = [
		('depth', X.INT8),
		('visual_id', X.ID)
		]

class EncodingInfo(ctypes.Structure):
	_fields_ = [
		('encoding_id', Encoding),
		('name', X.STRING8),
		('width', X.INT32),
		('height', X.INT32),
		('rate_numerator', X.INT),
		('rate_denominator', X.INT),
		('num_encodings', X.INT32)
		]

class AdaptorInfo(ctypes.Structure):
	_fields_ = [
		('base_id', Port),
		('n_ports', X.INT32),
		('type', X.BYTE),
		('name', X.STRING8),
		('n_formats', X.INT32),
		('formats', X.ArrayOf(Format)),
		('n_adaptors', X.INT32)
		]

class ImageFormatValues(ctypes.Structure):
	_fields_ = [
		('id', X.CARD32),
		('type', X.CARD8),
		('byte_order', X.CARD8),
		('pad1', X.CARD16),
		('guid', X.CARD8*16),
		('bpp', X.CARD8),
		('n_planes', X.CARD8),
		('pad2', X.CARD16),
		('depth', X.CARD8),
		('pad3', X.CARD8),
		('pad4', X.CARD16),
		('red_mask', X.Bitmask),
		('green_mask', X.Bitmask),
		('blue_mask', X.Bitmask),
		('format', X.CARD8),
		('pad5', X.CARD8),
		('pad6', X.CARD16),
		('y_sample_bits', X.CARD32),
		('u_sample_bits', X.CARD32),
		('v_sample_bits', X.CARD32),
		('horz_y_period', X.CARD32),
		('horz_u_period', X.CARD32),
		('horz_v_period', X.CARD32),
		('vert_y_period', X.CARD32),
		('vert_u_period', X.CARD32),
		('vert_v_period', X.CARD32),
		('comp_order', X.CARD8*32),
		('scanline_order', X.CARD8),
		('pad7', X.CARD8),
		('pad8', X.CARD16),
		('pad9', X.CARD32),
		('pad10', X.CARD32)
		]

class Image(ctypes.Structure):
	_fields_ = [
		('id', X.INT),
		('width', X.INT),
		('height', X.INT),
		('data_size', X.INT),
		('n_planes', X.INT),
		('pitches', X.AddressOf(X.INT)),
		('offsets', X.AddressOf(X.INT)),
		('data', X.String),
		('obdata', X.Pointer)
		]

# Events

class VideoNotify(ctypes.Structure):
	_fields_ = [
		('type', X.INT),
		('serial', X.CARD32),
		('send_event', X.BOOL),
		('display', X.Display),
		('drawable', X.Drawable),
		('reason', X.Bitmask),
		('port_id', Port),
		('time', X.Time)
		]

class PortNotify(ctypes.Structure):
	_fields_ = [
		('type', X.INT),
		('serial', X.CARD32),
		('send_event', X.BOOL),
		('display', X.Display),
		('port_id', Port),
		('time', X.Time),
		('attribute', X.Atom),
		('value', X.INT32)
		]

from X11.event import Event
Event._fields_.append(VideoNotify)
Event._fields_.append(PortNotify)

# Functions

Callable = X.Wrapper('Xv')


X.Display.QueryVideoExtension = Callable(
	'XvQueryExtension', int,
	['self', X.Display],
	['return_version', X.CARD],
	['return_revision', X.CARD],
	['return_request_base', X.CARD],
	['return_event_base', X.CARD],
	['return_error_base', X.CARD]
	)



X.Display.QueryAdaptors = Callable(
	'XvQueryAdaptors', int,
	['self', X.Display],
	['window', X.Window],
	['return_n', X.CARD],
	['return_adaptors', X.ArrayOf(AdaptorInfo)]
	)

FreeAdaptorInfo = Callable(
	'XvFreeAdaptorInfo', None,
	['adaptor', X.AddressOf(AdaptorInfo)]
	)

def QueryAdaptors(window):
	n, p = window.QueryAdaptors();
	for i in range(n):
		yield p[i]
	FreeAdaptorInfo(p)

X.Window.adaptors = property(QueryAdaptors)

X.Display.QueryEncodings = Callable(
	'XvQueryEncodings', int,
	['self', X.Display],
	['port', Port],
	['return_n', X.CARD],
	['return_encodings', X.ArrayOf(EncodingInfo)]
	)

FreeEncodingInfo = Callable(
	'XvFreeEncodingInfo', None,
	['encoding', X.AddressOf(EncodingInfo)]
	)

def QueryEncodings(port):
	n, p = port.QueryEncodings()
	for i in range(n):
		yield p[i]
	FreeEncodingInfo(p)

Port.encodings = property(QueryEncodings)

X.Display.QueryPortAttributes = Callable(
	'XvQueryPortAttributes', X.AddressOf(Attribute),
	['self', X.Display],
	['port', Port],
	['count', X.ByRef(X.INT)]
	)

def QueryPortAttributes(port):
	n = X.INT()
	attr = port.QueryPortAttributes(n)
	for i in range(n.value):
		yield attr[i]
	X.Free(attr)

Port.attributes = property(QueryPortAttributes)

X.Display.ListImageFormats = Callable(
	'XvListImageFormats', X.ArrayOf(ImageFormatValues),
	['self', X.Display],
	['port', Port],
	['count', X.ByRef(X.INT)]
	)

def ListImageFormats(port):
	n = X.INT()
	fmt = port.ListImageFormats(n)
	for i in range(n.value):
		yield fmt[i]
	X.Free(fmt)

Port.image_formats = property(ListImageFormats)



X.Display.PutVideo = Callable(
	'XvPutVideo', int,
	['self', X.Display],
	['port', Port],
	['drawable', X.Drawable],
	['gc', X.GC],
	['vx', X.Integer],
	['vy', X.Integer],
	['vwidth', X.Integer],
	['vheight', X.Integer],
	['dx', X.Integer],
	['dy', X.Integer],
	['dwidth', X.Integer],
	['dheight', X.Integer]
	)

X.Display.PutStill = Callable(
	'XvPutStill', int,
	['self', X.Display],
	['port', Port],
	['drawable', X.Drawable],
	['gc', X.GC],
	['vx', X.Integer],
	['vy', X.Integer],
	['vwidth', X.Integer],
	['vheight', X.Integer],
	['dx', X.Integer],
	['dy', X.Integer],
	['dwidth', X.Integer],
	['dheight', X.Integer]
	)


X.Display.GetVideo = Callable(
	'XvPutVideo', int,
	['self', X.Display],
	['port', Port],
	['drawable', X.Drawable],
	['gc', X.GC],
	['vx', X.Integer],
	['vy', X.Integer],
	['vwidth', X.Integer],
	['vheight', X.Integer],
	['dx', X.Integer],
	['dy', X.Integer],
	['dwidth', X.Integer],
	['dheight', X.Integer]
	)

X.Display.GetStill = Callable(
	'XvPutStill', int,
	['self', X.Display],
	['port', Port],
	['drawable', X.Drawable],
	['gc', X.GC],
	['vx', X.Integer],
	['vy', X.Integer],
	['vwidth', X.Integer],
	['vheight', X.Integer],
	['dx', X.Integer],
	['dy', X.Integer],
	['dwidth', X.Integer],
	['dheight', X.Integer]
	)

X.Display.StopVideo = Callable(
	'XvStopVideo', int,
	['self', X.Display],
	['port', Port],
	['drawable', X.Drawable]
	)

X.Display.GrabPort = Callable(
	'XvGrabPort', int,
	['self', X.Display],
	['port', Port],
	['time', X.Time, X.CurrentTime]
	)

X.Display.UngrabPort = Callable(
	'XvUngrabPort', int,
	['self', X.Display],	
	['port', Port],
	['time', X.Time, X.CurrentTime]
	)

X.Display.SelectVideoNotify = Callable(
	'XvSelectVideoNotify', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['enable', X.BOOL, True]
	)

X.Display.SelectPortNotify = Callable(
	'XvSelectPortNotify', int,
	['self', X.Display],
	['port', Port],
	['enable', X.BOOL, True]
	)

X.Display.SetPortAttribute = Callable(
	'XvSetPortAttribute', int,
	['self', X.Display],
	['port', Port],
	['atom', X.Atom],
	['value', X.Integer]
	)

X.Display.GetPortAttribute = Callable(
	'XvGetPortAttribute', int,
	['self', X.Display],
	['port', Port],
	['atom', X.Atom],
	['return_value', X.INT]
	)

X.Display.QueryBestVideoSize = Callable(
	'XvQueryBestSize', int,
	['self', X.Display],
	['port', Port],
	['motion', X.BOOL],
	['vwidth', X.Integer],
	['vheight', X.Integer],
	['dwidth', X.Integer],
	['dheight', X.Integer],
	['return_width', X.INT],
	['return_height', X.INT]
	)

X.Display.CreateVideoImage = Callable(
	'XvCreateImage', X.AddressOf(Image),
	['self', X.Display],
	['port', Port],
	['id', X.Integer],
	['data', X.String],
	['width', X.Integer],
	['height', X.Integer]
	)

X.Display.PutVideoImage = Callable(
	'XvPutImage', int,
	['self', X.Display],
	['port', Port],
	['drawable', X.Drawable],
	['gc', X.GC],
	['image', X.ByRef(Image)],
	['src_x', X.Integer],
	['src_y', X.Integer],
	['src_width', X.Integer],
	['src_height', X.Integer],
	['dst_x', X.Integer],
	['dst_y', X.Integer],
	['dst_width', X.Integer],
	['dst_height', X.Integer]
	)

# XvShmCreateImage
# XvShmPutImage

