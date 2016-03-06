#!/usr/bin/env python
"""Reads a pixmap from file and draws it to a window"""

import X11
from X11 import display, window, event, xpm

dpy = X11.Open()

#Xpm is a C coded format for icon or cursor images
pix, mask, attr = dpy.root.ReadPixmapFile('X.xpm')

wnd = dpy.root.CreateSimpleWindow(width = attr.width, height = attr.height)
wnd.SetWindowBackgroundPixmap(pix)
wnd.MapRaised()

for e in dpy:
	pass

