import X11 as X


X.Display.RegisterIMInstantiateCallback = X.Callable(
	'XRegisterIMInstantiateCallback', bool,
	['self', X.Display],
	['db', X.Database],
	['res_name', X.String],
	['res_class', X.String],
	['callback', Procedure],
	['userdata', X.Pointer]
	)
	
X.Display.UnregisterIMInstantiateCallback = X.Callable(
	'XUnregisterIMInstantiateCallback', bool,
	['self', X.Display],
	['db', X.Database],
	['res_name', X.String],
	['res_class', X.String],
	['callback', Procedure],
	['userdata', X.Pointer]
	)
	
X.IC.SetFocus = X.Callable(
	'XSetICFocus', None,
	['self', X.IC]
	)
	
X.IC.UnsetFocus = X.Callable(
	'XUnsetICFocus', None,
	['self', X.IC]
	)


### Input Method ##############################################


X.Display.OpenIM = X.Callable(
	'XOpenIM', X.IM,
	['self', X.Display],
	['db', X.Database],
	['res_name', X.String],
	['res_class', X.String]
	)
	
X.IM.Close = X.Callable(
	'XCloseIM', X.Status,
	['self', X.IM]
	)
	
X.IM.SetValues = VaX.Callable(
	'XSetIMValues', X.String,
	['self', X.IM]
	)
	
X.IM.GetValues = VaX.Callable(
	'XGetIMValues', X.String,
	['self', X.IM]
	)
	
X.IM.display = X.extern_property('XDisplayOfIM', X.Display)

X.IM.locale = X.extern_property('XLocaleOfIM', X.STRING8)


### Input Context #############################################


X.IM.CreateIC = VaX.Callable(
	'XCreateIC', X.IC,
	['self', X.IM]
	)
	
X.IC.Destroy = X.Callable(
	'XDestroyIC', None
	['self', X.IC]
	)
	
X.IC.SetValues = VaX.Callable(
	'XSetICValues', X.String,
	['self', X.IC]
	)
	
X.IC.GetValues = VaX.Callable(
	'XGetICValues', X.String,
	['self', X.IC]
	)
	
X.IC.method = X.extern_property('XIMOfIC', X.IM)


### Output Method #############################################


X.Display.OpenOM = X.Callable(
	'XOpenOM', X.OM,
	['self', X.Display],
	['db', X.Database],
	['res_name', X.String],
	['res_class', X.String]
	)
	
X.OM.Close = X.Callable(
	'XCloseOM', X.Status,
	['self', X.OM]
	)
	
X.OM.SetValues = VaX.Callable(
	'XSetOMValues', X.String,
	['self', X.OM]
	)
	
X.OM.GetValues = VaX.Callable(
	'XGetOMValues', X.String,
	['self', X.OM]
	)
	
X.OM.display = X.extern_property('XDisplayOfOM', X.Display)

X.OM.locale = X.extern_property('XLocaleOfOM', X.STRING8)


### Output Context ############################################


X.OM.CreateOC = X.Callable(
	'XCreateOC', X.OC,
	['self', X.OM]
	)
	
X.OC.Destroy = X.Callable(
	'XDestroyOC', None,
	['self', X.OC]
	)
	
X.OC.SetValues = VaX.Callable(
	'XSetOCValues', X.String,
	['self', X.OC]
	)
	
X.OC.GetValues = VaX.Callable(
	'XGetOCValues', X.String,
	['self', X.OC]
	)
	
X.OC.method = X.extern_property('XOMOfOC', X.OM)

