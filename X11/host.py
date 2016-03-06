import X11 as X, ctypes

class HostAddress(ctypes.Structure):
	_fields_ = [
		('family', X.CARD),
		('length', X.INT),
		('address', X.STRING8)
		]
		
X.Display.ListHosts = X.Callable(
	'XListHosts', X.ArrayOf(HostAddress),
	['self', X.Display],
	['count', X.ByRef(X.INT)],
	['state', X.ByRef(X.BOOL)]
	)
	
def HostList(display):
	n = X.INT()
	state = X.CARD()
	addr = display.ListHosts(n, state)
	for i in range(n.value):
		yield addr[i]
	X.Free(addr)
	
X.Display.hosts = property(HostList)

X.Display.AddHost = X.Callable(
	'XAddHost', int,
	['self', X.Display],
	['host', X.ByRef(HostAddress)]
	)
	
X.Display.AddHosts = X.Callable(
	'XAddHosts', int,
	['self', X.Display],
	['hosts', X.ListOf(HostAddress)],
	['nhosts', X.Integer]
	)
	
X.Display.RemoveHost = X.Callable(
	'XRemoveHost', int,
	['self', X.Display],
	['host', X.ByRef(HostAddress)]
	)
	
X.Display.RemoveHosts = X.Callable(
	'XRemoveHosts', int,
	['self', X.Display],
	['hosts', X.ListOf(HostAddress)],
	['nhosts', X.Integer]
	)

X.Display.SetAccessControl = X.Callable(
	'XSetAccessControl', int,
	['self', X.Display],
	['enabled', X.BOOL, True]
	)
	
X.Display.EnableAccessControl = X.Callable(
	'XEnableAccessControl', int,
	['self', X.Display]
	)
	
X.Display.DisableAccessControl = X.Callable(
	'XDisableAccessControl', int,
	['self', X.Display]
	)
	
SetAuthorization = X.Callable(
	'XSetAuthorization', None,
	['name', X.String],
	['namelen', X.Integer],
	['data', X.String],
	['datalen', X.Integer]
	)	

