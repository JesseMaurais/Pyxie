#!/usr/bin/env python
"""Shows basic uses of event iterators"""

import X11
from X11 import display, window, event, atom

dpy = X11.Open()

wnd = dpy.root.CreateSimpleWindow()
wnd.SelectInput() #All input
wnd.MapRaised()

for e in dpy:
	#Tell us what event occurred
	print event.Type.name(e.type)

