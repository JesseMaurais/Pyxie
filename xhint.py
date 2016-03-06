#!/usr/bin/env python
"""Gives window manager hints for resize policy and tray/decorator icon"""

import X11
from X11 import display, window, event, hint, xpm

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow()

icon = wnd.ReadPixmapFile('X.xpm')
mask = wnd.ReadPixmapFile('X-mask.xpm')

wm_hints = hint.WindowManager(
	icon_pixmap = icon[0],
	icon_mask = mask[0],
	icon_window = wnd
	)

sz_hints = hint.Size(
	min_width = 300,
	max_width = 1000,
	inc_width = 100,
	min_height = 300,
	max_height = 1000,
	inc_height = 100,
	base_width = 10,
	base_height = 10,
	min_aspect_x = 1,
	min_aspect_y = 10,
	max_aspect_x = 10,
	max_aspect_y = 1,
	win_gravity = window.Gravity.Center
	)

wnd.SetWMHints(wm_hints)
wnd.SetWMNormalHints(sz_hints)
wnd.MapRaised()

for e in dpy:
	pass

