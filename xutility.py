#!/usr/bin/env python
"""Demonstrate the use of several utility functions"""

import X11
from X11 import display, screen, window, event, graphic
from X11.utility import drawable, window, pixmap

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow(width=640, height=480)
scn = wnd.screen

#This equality should hold
assert scn.value == dpy.screen.value

#These are for coloring
fg = wnd.CreateGC()
fg.SetForeground(scn.black)
bg = wnd.CreateGC()
bg.SetForeground(scn.white)

#Tiny pixmap drawn with a checker-board pattern
pix = scn.CreateStipplePixmap(scn.white, scn.black)

wnd.SetWindowBackgroundPixmap(pix)
wnd.SelectInput(event.Mask.Exposure)
wnd.MapRaised()

for e in dpy:
	if e.type is event.Type.Expose:
		#Bevelled edges are all the rage these days
		wnd.FillRoundedRectangle(fg, 140, 90,  360, 280,  90, 90)
		wnd.FillRoundedRectangle(bg, 160, 110,  320, 240,  40, 40)
		#Low resolution (aliased) X11 logo
		wnd.DrawLogo(fg, bg,  220, 130,  200, 200)

