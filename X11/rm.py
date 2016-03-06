import X11 as X, bit, ctypes


X.Callable.lib.XrmInitialize()


### Quark #####################################################


class Quark(X.Cardinal):
	pass

class Binding(X.Cardinal):
	pass

UniqueQuark = X.Callable(
	'XrmUniqueQuark', Quark
	)

StringToQuark = X.Callable(
	'XrmStringToQuark', Quark,
	['string', X.String]
	)
	
QuarkToString = X.Callable(
	'XrmQuarkToString', X.STRING8,
	['quark', Quark]
	)	

StringToQuarkList = X.Callable(
	'XrmStringToQuarkList', None,
	['string', X.String],
	['quarks', X.ArrayOf(Quark)]
	)
	
Bind = bit.enum('Tightly Loosely')
	
StringToBindingQuarkList = X.Callable(
	'XrmStringToBindingQuarkList', None,
	['string', X.String],
	['bindings_out', X.ArrayOf(Binding)],
	['quarks_out', X.ArrayOf(Quark)]
	)

	
### Database ##################################################


GetStringDatabase = X.Callable(
	'XrmGetStringDatabase', X.Database,
	['data', X.String]
	)

PutFileDatabase = X.Callable(
	'XrmPutFileDatabase', None,
	['db', X.Database],
	['filename', X.String]
	)
	
GetFileDatabase = X.Callable(
	'XrmGetFileDatabase', X.Database,
	['filename', X.String]
	)
	
CombineFileDatabase = X.Callable(
	'XrmCombineFileDatabase', X.Status,
	['filename', X.String],
	['target', X.ByRef(X.Database)],
	['override', X.BOOL, True]
	)


X.Display.SetDatabase = X.Callable(
	'XrmSetDatabase', None,
	['self', X.Display],
	['db', X.Database]
	)
	
X.Display.GetDatabase = X.Callable(
	'XrmGetDatabase', X.Database,
	['self', X.Display]
	)
	
X.Display.database = property(X.Display.GetDatabase, X.Display.SetDatabase)

X.Database.Destroy = X.Callable(
	'XrmDestroyDatabase', None,
	['self', X.Database]
	)
		
X.Database.Combine = X.Callable(
	'XrmCombineDatabase', None,
	['self', X.Database],
	['with', X.ByRef(X.Database)],
	['override', X.BOOL, True]
	)
	
X.Database.Merge = X.Callable(
	'XrmMergeDatabases', None,
	['self', X.Database],
	['with', X.ByRef(X.Database)]
	)

X.Database.locale = X.extern_property('XrmLocaleOfDatabase', X.STRING8)


### Resource ##################################################

	
class Value(ctypes.Structure):
	_fields_ = [
		('size', X.CARD),
		('addr', X.STRING8)
		]
	def __init__(self, data):
		self.size = ctypes.sizeof(data)
		self.addr = ctypes.addressof(data)
	

X.Database.QPutResource = X.Callable(
	'XrmQPutResource', None,
	['self', X.ByRef(X.Database)],
	['bindings', X.ListOf(Bind)],
	['quarks', X.ListOf(Quark)],
	['representation', Quark],
	['value', X.ByRef(Value)]
	)
	
X.Database.QGetResource = X.Callable(
	'XrmQGetResource', bool,
	['self', X.Database],
	['quark_name', X.ListOf(Quark)],
	['quark_class', X.ListOf(Quark)],
	['quark_type_return', Quark],
	['value_return', Value]
	)

X.Database.PutResource = X.Callable(
	'XrmPutResource', None,
	['self', X.ByRef(X.Database)],
	['specifier', X.String],
	['type', X.String],
	['Value', X.ByRef(Value)]
	)
		
X.Database.GetResource = X.Callable(
	'XrmGetResource', bool,
	['self', X.Database],
	['string_name', X.String],
	['string_class', X.String],
	['string_type_return', X.String],
	['value_return', Value]
	)
			
X.Database.QPutStringResource = X.Callable(
	'XrmQPutStringResource', None,
	['self', X.ByRef(X.Database)],
	['bindings', X.ListOf(Bind)],
	['quarks', X.ListOf(Quark)],
	['value', X.String]
	)
	
X.Database.PutStringResource = X.Callable(
	'XrmPutStringResource', None,
	['self', X.ByRef(X.Database)],
	['specifier', X.String],
	['value', X.String]
	)

X.Database.PutLineResource = X.Callable(
	'XrmPutLineResource', None,
	['self', X.ByRef(X.Database)],
	['line', X.String]
	)


### Enumeration ###############################################


Enumerator = ctypes.CFUNCTYPE(
	X.BOOL,
	X.Database,
	X.ArrayOf(Binding),
	X.ArrayOf(Quark),
	X.AddressOf(Quark),
	X.AddressOf(Value),
	X.Pointer
	)

X.Database.Enumerate = X.Callable(
	'XrmEnumerateDatabase', bool,
	['name_prefix', X.ArrayOf(Quark)],
	['class_prefix', X.ArrayOf(Quark)],
	['one_level', X.BOOL],
	['predicate', Enumerator],
	['arg', X.Pointer, None]
	)

# XrmPermStringToQuark
# XrmQGetSearchList
# XrmQGetSearchResource




