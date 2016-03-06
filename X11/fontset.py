import X11 as X, ctypes
from fontquery import FontStruct

class Extents(ctypes.Structure):
	_fields_ = [
		('max_ink_extent', X.Rectangle),
		('max_logical_extent', X.Rectangle)
		]

X.Display.CreateFontSet = X.Callable(
	'XCreateFontSet', X.FontSet,
	['self', X.Display],
	['base_font_name_list', X.String],
	['missing_charset_list', X.ByRef(X.ArrayOf(X.STRING8))],
	['missing_charset_count', X.ByRef(X.INT)],
	['default_string', X.ByRef(X.STRING8)]
	)
	
X.Display.FreeFontSet = X.Callable(
	'XFreeFontSet', None,
	['self', X.Display],
	['fontset', X.FontSet]
	)

X.FontSet.Fonts = X.Callable(
	'XFontsOfFontSet', int,
	['self', X.FontSet],
	['return_fontstruct_list', X.ArrayOf(FontStruct)],
	['return_font_name_list', X.ArrayOf(X.STRING8)]
	)

X.FontSet.extents = X.extern_property('XExtentsOfFontSet', X.AddressOf(Extents))

X.FontSet.base_font_name_list = X.extern_property('XBaseFontNameListOfFontSet', X.STRING8)

X.FontSet.locale = X.extern_property('XLocaleOfFontSet', X.STRING8)

X.FontSet.contextual_drawing = X.extern_property('XContextualDrawing', bool)

X.FontSet.context_dependent_drawing = X.extern_property('XContextDependentDrawing', bool)

X.FontSet.directional_dependent_drawing = X.extern_property('XDirectionalDependentDrawing', bool)


