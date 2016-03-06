
__all__ = [
	'fixes',
	'GLX',
	'composite',
	'damage',
	'ext',
	'group',
	'render',
	'shape',
	'video'
	]

import X11 as X

X.Display.QueryExtension = X.Callable(
	'XQueryExtension', bool,
	['self', X.Display],
	['name', X.String],
	['return_major_opcode', X.CARD],
	['return_first_event', X.CARD],
	['return_first_error', X.CARD]
	)
	
X.Display.ListExtensions = X.Callable(
	'XListExtensions', X.ArrayOf(X.STRING8),
	['self', X.Display],
	['count', X.ByRef(X.INT)]
	)

def ExtensionList(display):
	n = X.INT()
	ext = display.ListExtensions(n)
	for i in range(n.value):
		yield ext[i]
	X.FreeExtensionList(ext)
	
X.Display.extensions = property(ExtensionList)
