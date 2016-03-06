#!/usr/bin/env python
"""Minimum code required to make and show a new window"""

import X11, time
from X11 import display, window

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow()
wnd.MapWindow()
dpy.Flush()

time.sleep(9)

wnd.UnmapWindow()
wnd.DestroyWindow()
dpy.Close()

