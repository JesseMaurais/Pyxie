import X11 as X, ctypes
from font import CharStruct

class FontProperty(ctypes.Structure):
	_fields_ = [
		('name', X.Atom),
		('card32', X.CARD32)
		]

class FontStruct(ctypes.Structure):
	_fields_ = [
		('ext_data', X.Pointer),
		('fid', X.Font),
		('direction', X.CARD),
		('min_char_or_byte2', X.CARD),
		('max_char_or_byte2', X.CARD),
		('min_byte1', X.CARD),
		('max_byte1', X.CARD),
		('all_chars_exist', X.BOOL),
		('default_char', X.CARD),
		('n_properties', X.INT),
		('properties', X.AddressOf(FontProperty)),
		('min_bounds', CharStruct),
		('max_bounds', CharStruct),
		('per_char', X.AddressOf(CharStruct)),
		('ascent', X.INT),
		('descent', X.INT)
		]
	
X.Display.QueryFont = X.Callable(
	'XQueryFont', X.AddressOf(FontStruct),
	['self', X.Display],
	['font', X.Font]
	)
	
X.Display.LoadQueryFont = X.Callable(
	'XLoadQueryFont', X.AddressOf(FontStruct),
	['self', X.Display],
	['name', X.String]
	)
	
X.Display.FreeFont = X.Callable(
	'XFreeFont', int,
	['self', X.Display],
	['fontstruct', X.AddressOf(FontStruct)]
	)
	
FontStruct.TextWidth = X.Callable(
	'XTextWidth', int,
	['self', X.ByRef(FontStruct)],
	['string', X.String],
	['strlen', X.Integer]
	)
	
FontStruct.TextWidth16 = X.Callable(
	'XTextWidth16', int,
	['self', X.ByRef(FontStruct)],
	['string', X.STRING16],
	['strlen', X.Integer]
	)

FontStruct.TextExtents = X.Callable(
	'XTextExtents', int,
	['self', X.ByRef(FontStruct)],
	['string', X.String],
	['strlen', X.Integer],
	['direction_return', X.INT],
	['font_ascent_return', X.INT],
	['font_descent_return', X.INT],
	['overall_return', CharStruct]
	)
	
FontStruct.TextExtents16 = X.Callable(
	'XTextExtents', int,
	['self', X.ByRef(FontStruct)],
	['string', X.STRING16],
	['strlen', X.Integer],
	['direction_return', X.INT],
	['font_ascent_return', X.INT],
	['font_descent_return', X.INT],
	['overall_return', CharStruct]
	)
	
FontStruct.GetFontProperty = X.Callable(
	'XGetFontProperty', bool,
	['self', X.ByRef(FontStruct)],
	['atom', X.Atom],
	['return', X.INT]
	)
	
