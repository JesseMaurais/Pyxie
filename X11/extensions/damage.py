import X11 as X
from X11.extensions import fixes

class Damage(X.ID):
	pass

X.Display.QueryDamageExtension = Callable(
	'XQueryDamageExtension', bool,
	['self', X.Display],
	['return_major', X.INT],
	['return_minor', X.INT]
	)

X.Display.QueryDamageVersion = Callable(
	'XDamageQueryVersion', X.Status,
	['self', X.Display],
	['return_major', X.INT],
	['return_minor', X.INT]
	)

Report = bit.enum(
	"""
	RawRectangles
	DeltaRectangles
	BoundingBox
	NonEmpty
	"""
	)

X.Display.CreateDamage = Callable(
	'XDamageCreate', Damage,
	['self', X.Display],
	['drawable', X.Drawable],
	['level', X.Cardinal, Report.RawRectangles]
	)

X.Display.DestroyDamage = Callable(
	'XDestroyDamage', None,
	['self', X.Display],
	['damage', Damage]
	)

X.Display.DamageSubtract = Callable(
	'XDamageSubtract', None,
	['self', X.Display],
	['damage', Damage],
	['repair', fixes.Region],
	['parts', fixes.Region]
	)

X.Display.DamageAdd = Callable(
	'XDamageAdd', None,
	['self', X.Display],
	['drawable', X.Drawable],
	['region', fixes.Region]
	)

