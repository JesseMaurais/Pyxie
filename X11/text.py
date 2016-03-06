import X11 as X, bit, ctypes

class TextProperty(ctypes.Structure):
	_fields_ = [
		('value', X.STRING8),
		('encoding', X.Atom),
		('format', X.INT),
		('nitems', X.INT)
		]
		
class TextItem(ctypes.Structure):
	_fields_ = [
		('chars', X.STRING8),
		('nchars', X.INT),
		('delta', X.INT),
		('font', X.Font)
		]
		
class TextItem16(ctypes.Structure):
	_fields_ = [
		('chars', X.STRING16),
		('nchars', X.INT),
		('delta', X.INT),
		('font', X.Font)
		]

EncodingStyle = bit.enum(
	"""
	String
	CompoundText
	Text
	ICCText
	UTF8String
	"""
	)
	
X.Display.DrawText = X.Callable(
	'XDrawText', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['items', X.AddressOf(TextItem)],
	['nitems', X.Integer]
	)

X.Display.DrawText16 = X.Callable(
	'XDrawText', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['items', X.AddressOf(TextItem16)],
	['nitems', X.Integer]
	)
	
X.Display.GetTextProperty = X.Callable(
	'XGetTextProperty', X.Status,
	['self', X.Display],
	['window', X.Window],
	['return', TextProperty],
	['property', X.Atom]
	)
	
X.Display.SetTextProperty = X.Callable(
	'XSetTextProperty', None,
	['self', X.Display],
	['window', X.Window],
	['text', X.AddressOf(TextProperty)],
	['property', X.Atom]
	)

PropertyToStringList = X.Callable(
	'XTextPropertyToStringList', X.Status,
	['text', X.AddressOf(TextProperty)],
	['string_list_return', X.ArrayOf(X.STRING8)],
	['count_return', X.INT32]
	)

StringListToProperty = X.Callable(
	'XStringListToTextProperty', X.Status,
	['string_list', X.ArrayOf(X.String)],
	['text', X.ByRef(TextProperty)]
	)

