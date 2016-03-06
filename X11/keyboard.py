import X11 as X, bit, ctypes

KB = bit.mask(
	"""
	KeyClickPercent
	BellPercent
	BellPitch
	BellDuration
	Led
	LedMode
	Key
	AutoRepeatMode
	"""
	)

AutoRepeatMode = bit.enum('Off On Default')

class Control(ctypes.Structure):
	_fields_ = [
		('key_click_percent', X.INT),
		('bell_percent', X.INT),
		('bell_pitch', X.INT),
		('bell_duration', X.INT),
		('led', X.INT),
		('led_mode', X.INT),
		('key', X.INT),
		('auto_repeat_mode', X.CARD)
		]
		
def MaskControl(**args):
	typemap = {
		'key_click_percent':KB.KeyClickPercent,
		'bell_percent':KB.BellPercent,
		'bell_pitch':KB.BellPitch,
		'bell_duration':KB.BellDuration,
		'led':KB.Led,
		'led_mode':KB.LedMode,
		'key':KB.Key,
		'auto_repeat_mode':KB.AutoRepeatMode
		}
	mask = 0
	for key in args:
		mask |= typemap[key]
	return mask, Control(**args)

class State(ctypes.Structure):
	_fields_ = [
		('key_click_percent', X.INT),
		('bell_percent', X.INT),
		('bell_pitch', X.INT),
		('bell_duration', X.INT),
		('led_mask', X.Bitmask),
		('global_auto_repeat', X.CARD),
		('auto_repeats', X.BYTE*32)
		]

X.Display.ChangeKeyboardControl = X.Callable(
	'XChangeKeyboardControl', int,
	['self', X.Display],
	['mask', X.Bitmask],
	['values', X.ByRef(Control)]
	)
	
X.Display.GetKeyboardControl = X.Callable(
	'XGetKeyboardControl', int,
	['self', X.Display],
	['return', State]
	)

X.Display.AutoRepeatOn = X.Callable(
	'XAutoRepeatOn', int,
	['self', X.Display]
	)
	
X.Display.AutoRepeatOff = X.Callable(
	'XAutoRepeatOff', int,
	['self', X.Display]
	)
	
X.Display.QueryKeymap = X.Callable(
	'XQueryKeymap', int,
	['self', X.Display],
	['keys', X.ByRef(X.BYTE)]
	)
	
X.Display.Bell = X.Callable(
	'XBell', int,
	['self', X.Display],
	['percent', X.Integer, 100]
	)

