#!/usr/bin/env python
import X11
from X11 import display, screen, window, event, graphic, drawable

dpy = X11.Open()

wnd = dpy.root.CreateSimpleWindow(
	50, 50, # origin
	200, 200, # size
	0, dpy.screen.black, # border
	dpy.screen.white # background
	)

dpy.MapWindow(wnd)
wnd.SelectInput(event.Mask.StructureNotify)

for e in dpy:

	if e.type is event.Type.MapNotify:

		gc = wnd.CreateGC()
		gc.SetForeground(dpy.screen.black)
		wnd.DrawLine(gc, 10, 10, 190, 190)
		wnd.DrawLine(gc, 10, 190, 190, 10)
		wnd.SelectInput(event.Mask.ButtonPress)

	if e.type is event.Type.ButtonPress:

		dpy.DestroyWindow(wnd)
		dpy.Close()
		break


