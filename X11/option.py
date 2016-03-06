import X11 as X, bit
	
Kind = bit.enum(
	"""
	NoArg
	IsArg
	StickyArg
	SepArg
	ResArg
	SkipArg
	SkipLine
	SkipNArgs
	"""
	)
	
class Option(ctypes.Structure):
	_fields_ = [
		('option', X.STRING8),
		('specifier', X.STRING8),
		('kind', X.CARD),
		('value', X.AddressOf(Value))
		]
		
X.Database.ParseCommand = X.Callable(
	'XrmParseCommand', None,
	['self', X.ByRef(X.Database)],
	['desc', X.ListOf(Option)],
	['ndesc', X.Integer],
	['name', X.String],
	['argc', X.ByRef(X.INT)],
	['argv', X.ByRef(X.ArrayOf(X.STRING8))]
	)

