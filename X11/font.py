import X11 as X, ctypes

class CharStruct(ctypes.Structure):
	_fields_ = [
		('lbearing', X.INT16),
		('rbearing', X.INT16),
		('width', X.INT16),
		('height', X.INT16),
		('ascent', X.INT16),
		('descent', X.INT16),
		('attributes', X.CARD16)
		]

X.Display.LoadFont = X.Callable(
	'XLoadFont', X.Font,
	['self', X.Display],
	['name', X.String]
	)
	
X.Display.UnloadFont = X.Callable(
	'XUnloadFont', int,
	['self', X.Display],
	['font', X.Font]
	)
	
X.Display.ListFonts = X.Callable(
	'XListFonts', X.ArrayOf(X.STRING8),
	['self', X.Display],
	['pattern', X.String],
	['maxnames', X.Integer],
	['count', X.ByRef(X.INT)]
	)
	
def FontsList(display, pattern='*', max=65535):
	n = X.INT()
	font = display.ListFonts(pattern, max, n)
	for i in range(n.value):
		yield font[i]
	X.FreeFontNames(font)
	
X.Display.fonts = property(FontsList)
	
X.Display.SetFontPath = X.Callable(
	'XSetFontPath', int,
	['self', X.Display],
	['directories', X.ListOf(X.String)],
	['n_directories', X.Integer]
	)
	
X.Display.GetFontPath = X.Callable(
	'XGetFontPath', X.ArrayOf(X.STRING8),
	['self', X.Display],
	['count', X.ByRef(X.INT)]
	)

X.Display.QueryTextExtents = X.Callable(
	'XQueryTextExtents', int,
	['self', X.Display],
	['font', X.Font],
	['string', X.String],
	['strlen', X.Integer],
	['return_direction', X.INT],
	['return_font_ascent', X.INT],
	['return_font_descent', X.INT],
	['return_overall', CharStruct]
	)
	
X.Display.QueryTextExtents16 = X.Callable(
	'XQueryTextExtents', int,
	['self', X.Display],
	['font', X.ID],
	['string', X.STRING16],
	['strlen', X.Integer],
	['return_direction', X.INT],
	['return_font_ascent', X.INT],
	['return_font_descent', X.INT],
	['return_overall', CharStruct]
	)

