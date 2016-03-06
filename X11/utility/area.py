
New = Callable(
	'XmuNewArea', Area,
	['x', X.Integer, 0],
	['y', X.Integer, 0],
	['width', X.Integer, 0],
	['height', X.Integer, 0]
	)

Area.Duplicate = Callable(
	'XmuAreaDup', Area,
	['self', Area]
	)

Area.Copy = Callable(
	'XmuAreaCopy', Area,
	['self', Area],
	['other', Area]
	)

Area.Not = Callable(
	'XmuAreaNot', Area,
	['self', Area],
	['x', X.Integer],
	['y', X.Integer],
	['width', X.Integer],
	['height', X.Integer]
	)

Area.Or = Callable(
	'XmuAreaOrXor', Area,
	['self', Area],
	['other', Area],
	['include', X.BOOL, True]
	)

Area.Xor = Callable(
	'XmuAreaOrXor', Area,
	['self', Area],
	['other', Area],
	['include', X.BOOL, False]
	)

Area.And = Callable(
	'XmuAreaAnd'







