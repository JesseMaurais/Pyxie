#!/usr/bin/env python
"""Shows how to collect basic keyboard and mouse input"""

import X11
from X11 import display, window, event

dpy = X11.Open()

wnd = dpy.root.CreateSimpleWindow()
wnd.SelectInput(event.Mask('KeyPress ButtonPress'))
wnd.MapRaised()

for e in dpy:

	if e.type is event.Type.KeyPress:
		keysym = e.xkey.sym
		print 'KeySym:', chr(keysym) if keysym < 256 else keysym

	if e.type is event.Type.ButtonPress:
		print 'Button:', e.xbutton.button

