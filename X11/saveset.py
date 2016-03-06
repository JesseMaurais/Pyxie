import X11 as X

X.Display.ChangeSaveSet = X.Callable(
	'XChangeSaveSet', int,
	['self', X.Display],
	['window', X.Window],
	['delete', X.BOOL, False]
	)
	
X.Display.AddToSaveSet = X.Callable(
	'XAddToSaveSet', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.RemoveFromSaveSet = X.Callable(
	'XRemoveFromSaveSet', int,
	['self', X.Display],
	['window', X.Window]
	)
