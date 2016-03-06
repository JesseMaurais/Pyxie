import X11 as X

X.Display.ChangeKeyboardMapping = Callable(
	'XChangeKeyboardMapping', int,
	['self', X.Display],
	['first_keycode', X.KeyCode],
	['keysyms_per_keycode', X.Integer],
	['keysyms', ListOf(X.KeySym)],
	['nkeysyms', X.Integer]
	)
	
X.Display.GetKeyboardMapping = Callable(
	'XGetKeyboardMapping', ArrayOf(KeySym),
	['self', X.Display],
	['first_keycode', X.KeyCode],
	['count', X.Integer],
	['keysyms_per_keycode', ByRef(X.INT)]
	)

X.Display.SetModifierMapping = Callable(
	'XSetModifierMapping', int,
	['self', X.Display],
	['modmap', X.Keymap]
	)

X.Display.GetModifierMapping = Callable(
	'XGetModifierMapping', X.Keymap,
	['self', X.Display]
	)
	
X.Display.Keycodes = Callable(
	'XDisplayKeycodes', int,
	['self', X.Display],
	['min_keycodes_return', X.INT],
	['max_keycodes_return', X.INT]
	)
	
X.Display.keycodes = property(X.Display.Keycodes)

X.Keymap.__del__ = Callable(
	'XFreeModifiermap', int,
	['self', X.Keymap]
	)
	
X.Keymap.Insert = Callable(
	'XInsertModifiermapEntry', X.Keymap,
	['self', X.Keymap],
	['entry', X.KeyCode],
	['modifier', X.Integer]
	)
	
X.Keymap.Delete = Callable(
	'XDeleteModifiermapEntry', X.Keymap,
	['self', X.Keymap],
	['entry', X.KeyCode],
	['modifier', X.Integer]
	)
	
NewModifiermap = Callable(
	'XNewModifiermap', X.Keymap,
	['max_keys_per_mode', X.Integer]
	)
	
SupportsLocale = Callable(
	'XSupportsLocale', bool
	)
	
SetLocaleModifiers = Callable(
	'XSetLocaleModifiers', X.STRING8,
	['modifier_list', X.STRING8]
	)
	
