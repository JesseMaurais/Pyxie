#!/usr/bin/env python

import X11


width = 640
height = 480

mask, attr = render.MaskAttributes(
	poly_edge = render.PolyEdge.Smooth,
	poly_mode = render.PolyMode.Imprecise
	)

dpy = X11.Open()
fmt = dpy.screen.visual.format
wnd = dpy.root.CreateWindow()
pix = wnd.CreatePixmap()
pic = pix.CreatePicture(fmt, mask, attr)

wnd.SelectInput(event.Mask.StructureNotify)
wnd.SetWindowBackgroundPixmap(pix)
wnd.MapRaised()


def CreateBrush(r, g, b, a):

	mask, attr = render.MaskAttributes(repeat=True)
	col = render.Color(r, g, b, a)
	
	pix = wnd.CreatePixmap(1, 1, depth)
	pic = pix.CreatePicture(fmt, mask, attr)

	render.PictOp.Over.RenderFillRectangle(pic, col, 0, 0, 1, 1)
	dpy.FreePixmap(pix)

	return pic


def CreateCircle(x, y, radius, ntraps):

	traps = []
	for k in range(ntraps):
		trap = render.Trapezoid()
		traps.append(trap)



for e in dpy:
	if e.type is event.Type.Exp
	render.PictOp.Over.RenderFillRectangle(pic, black)
	
	XClearArea


			




