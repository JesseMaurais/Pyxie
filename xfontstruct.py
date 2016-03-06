#!/usr/bin/env python
import X11
from X11 import display, screen, window, event, fontquery, graphic, drawable, colormap

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow()
wnd.SelectInput(event.Mask.Exposure)
wnd.MapRaised()

fs = dpy.LoadQueryFont('*luxisans-medium-r*')
gc = dpy.screen.gc

gc.SetFont(fs[0].fid)
gc.SetForeground(dpy.screen.colormap.yellow)
gc.SetBackground(dpy.screen.colormap.brown)

msg = 'Hello World'

for e in dpy:
	if e.type is event.Type.Expose:
		wnd.DrawImageString(gc, 55, 89, msg, len(msg))

