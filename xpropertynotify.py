#!/usr/bin/env python
"""Shows basic uses of event iterators"""

import X11
from X11 import display, window, event, atom

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow()
wnd.SelectInput(event.Mask.PropertyChange)
wnd.MapRaised()

for e in dpy:
	if e.type is event.Type.PropertyNotify:
		print e.xproperty.selection.name

