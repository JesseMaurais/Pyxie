#!/usr/bin/env python
"""Shows window manager communication using WM_DELETE_WINDOW protocol"""

import X11
from X11 import display, window, event, atom, wm

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow()
wnd.MapRaised()

wnd.SetWMProtocols([dpy.WM_DELETE_WINDOW])

for e in dpy:
	if e.type is event.Type.ClientMessage:
	
		msg = e.xclient.data.l[0]

		if msg == dpy.WM_DELETE_WINDOW:
			print 'You clicked the window close button'
			break

dpy.Close()

