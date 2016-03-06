#!/usr/bin/env python
"""Demonstrate how a graphic context and colormap are used together"""

import X11
from X11 import display, screen, window, event, graphic, drawable, colormap

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow(width=220, height=100)
wnd.SelectInput(event.Mask.Exposure)
wnd.MapRaised()

gc = wnd.CreateGC()
gc.SetLineAttributes(
	7, graphic.Line.Solid, graphic.Cap.Round, graphic.Join.Round
	)
	
colors = dpy.screen.colormap

for e in dpy:
	if e.type is event.Type.Expose:

		gc.SetForeground(colors.red)
		wnd.DrawLine(gc, 20, 20, 70, 80)
		wnd.DrawLine(gc, 70, 20, 20, 80)

		gc.SetForeground(colors.green)
		wnd.FillRectangle(gc,  85, 20, 50, 60)
		
		gc.SetForeground(colors.blue)
		wnd.DrawRectangle(gc, 150, 20, 50, 60)

