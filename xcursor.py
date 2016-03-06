#!/usr/bin/env python
"""Shows some cursor functions using lame built-in font cursors"""

import X11
from X11 import window, event, cursor, screen, display


dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow()
wnd.SelectInput(event.Mask.ButtonPress)
wnd.MapRaised()

shape = 0
csr = dpy.CreateFontCursor(shape)
wnd.DefineCursor(csr)


print 'Click the window to change cursor shapes and I will print their names'

for e in dpy:
	if e.type is event.Type.ButtonPress:
		
		dpy.FreeCursor(csr)
		
		shape += 1
		if shape == cursor.Shapes.last:
			shape = 0
			
		csr = dpy.CreateFontCursor(shape)
		wnd.DefineCursor(csr)
			
		print cursor.Shapes.name(shape)

