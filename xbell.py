#!/usr/bin/env python

import X11
from X11 import display, window, event, keyboard

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow()
wnd.SelectInput(event.Mask.ButtonPress)
wnd.MapRaised()

print 'Click the window to hear the bell, or see it, depending on WM settings'

for e in dpy:
	if e.type is event.Type.ButtonPress:
		print 'press'
		dpy.Bell()

