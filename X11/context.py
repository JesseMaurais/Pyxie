import X11 as X


X.Display.UniqueContext = X.Callable(
	'XUniqueContext', int,
	)
	
X.Display.SaveContext = X.Callable(
	'XSaveContext', int,
	['self', X.Display],
	['context', X.Integer],
	['data', X.String]
	)
	
X.Display.FindContext = X.Callable(
	'XFindContext', int,
	['self', X.Display],
	['resource', X.ID],
	['context', X.Integer],
	['return', X.Pointer]
	)
	
X.Display.DeleteContext = X.Callable(
	'XDeleteContext', int,
	['self', X.Display],
	['resource', X.ID],
	['context', X.Integer]
	)
	
