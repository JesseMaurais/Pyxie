#!/usr/bin/env python
import X11
from X11 import display, window, event, pixmap, drawable, graphic
from X11.extensions import shape

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow(width=640, height=400)

#Pixmaps of depth 1 (bitmaps) serve as masks
pix = wnd.CreatePixmap(640, 400)
gc = pix.CreateGC()

#Bits that are on will be opaque
gc.SetForeground(True)
pix.FillRectangle(gc, 0, 0, 640, 400)
#Bits that are off will be transparent
gc.SetForeground(False)
pix.FillArc(gc, 120, 0, 400, 400, 0, 360 << 6)

#Now this pixmap will become the mask to define a window shape
wnd.CombineMask(shape.Kind.Bounding, 0, 0, pix, shape.Op.Set)
wnd.MapRaised()

for e in dpy:
	pass

