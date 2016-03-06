import X11 as X
from X11.extensions.fixes import Callable

class Region(X.ID):
	pass
	
X.Display.CreateRegion = Callable(
	'XFixesCreateRegion', Region,
	['self', X.Display],
	['rectangles', X.ArrayOf(X.Rectangle), None],
	['nrectangles', X.Integer, 0]
	)
	
X.Display.CreateRegionFromBitmap = Callable(
	'XFixesCreateRegionFromBitmap', Region,
	['self', X.Display],
	['bitmap', X.Pixmap]
	)
	
X.Display.CreateRegionFromWindow = Callable(
	'XFixesCreateRegionFromWindow', Region,
	['self', X.Display],
	['window', X.Window],
	['kind', X.Cardinal]
	)
	
X.Display.CreateRegionFromGC = Callable(
	'XFixesCreateRegionFromGC', Region,
	['self', X.Display],
	['gc', X.GC]
	)
	
X.Display.CreateRegionFromPicture = Callable(
	'XFixesCreateRegionFromPicture', Region,
	['self', X.Display],
	['picture', X.ID]
	)
	
X.Display.DestroyRegion = Callable(
	'XFixesDestroyRegion', None,
	['self', X.Display],
	['region', Region]
	)
	
X.Display.SetRegion = Callable(
	'XFixesSetRegion', None,
	['self', X.Display],
	['region', Region],
	['rectangles', X.ListOf(X.Rectangle)],
	['n_rectangles', X.Integer]
	)
	
X.Display.CopyRegion = Callable(
	'XFixesCopyRegion', None,
	['self', X.Display],
	['dst', Region],
	['src', Region]
	)
	
X.Display.UnionRegion = Callable(
	'XFixesUnionRegion', None,
	['self', X.Display],
	['dst', Region],
	['src1', Region],
	['src2', Region]
	)
	
X.Display.IntersectRegion = Callable(
	'XFixesIntersectRegion', None,
	['self', X.Display],
	['dst', Region],
	['src1', Region],
	['src2', Region]
	)
	
X.Display.SubtractRegion = Callable(
	'XFixesSubtractRegion', None,
	['self', X.Display],
	['dst', Region],
	['src1', Region],
	['src2', Region]
	)

X.Display.InvertRegion = Callable(
	'XFixesInvertRegion', None,
	['self', X.Display],
	['dst', Region],
	['rect', X.ByRef(X.Rectangle)],
	['src', Region]
	)
	
X.Display.TranslateRegion = Callable(
	'XFixesTranslateRegion', None,
	['self', X.Display],
	['region', Region],
	['dx', X.Integer],
	['dy', X.Integer]
	)
	
X.Display.ExpandRegion = Callable(
	'XFixesExpandRegion', None,
	['self', X.Display],
	['dst', Region],
	['src', Region],
	['left', X.Integer],
	['right', X.Integer],
	['top', X.Integer],
	['bottom', X.Integer]
	)
	
X.Display.RegionExtents = Callable(
	'XFixesRegionExtents', None,
	['self', X.Display],
	['dst', Region],
	['src', Region]
	)
	
X.Display.FetchRegion = Callable(
	'XFixesFetchRegion', X.ArrayOf(X.Rectangle),
	['self', X.Display],
	['region', Region],
	['count', X.ByRef(X.INT)]
	)
	
def FetchRegion(region):
	n = X.INT()
	rect = region.FetchRegion(n)
	for i in range(n.value):
		yield rect[i]
	X.Free(rect)
	
X.Region.fetch = property(FetchRegion)
	
# XFixesFetchRegionAndBounds

X.Display.SetGCClipRegion = Callable(
	'XFixesSetGCClipRegion', None,
	['self', X.Display],
	['gc', X.GC],
	['x', X.Integer],
	['y', X.Integer],
	['region', Region]
	)
	
X.Display.SetWindowShapeRegion = Callable(
	'XFixesSetWindowShapeRegion', None,
	['self', X.Display],
	['window', X.Window],
	['kind', X.Cardinal],
	['x', X.Integer],
	['y', X.Integer],
	['region', Region]
	)

X.Display.SetPictureClipRegion = Callable(
	'XFixesSetPictureClipRegion', None,
	['self', X.Display],
	['picture', X.ID],
	['x', X.Integer],
	['y', X.Integer],
	['region', Region]
	)

