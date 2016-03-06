import X11 as X

X.Display.SetSelectionOwner = X.Callable(
	'XSetSelectionOwner', int,
	['self', X.Display],
	['selection', X.Atom],
	['owner', X.Window],
	['time', X.Time, X.CurrentTime]
	)
	
X.Display.GetSelectionOwner = X.Callable(
	'XGetSelectionOwner', X.Window,
	['self', X.Display],
	['selection', X.Atom]
	)
	
X.Display.ConvertSelection = X.Callable(
	'XConvertSelection', int,
	['self', X.Display],
	['selection', X.Atom],
	['target', X.Atom],
	['property', X.Atom],
	['requestor', X.Window],
	['time', X.Time, X.CurrentTime]
	)
	
