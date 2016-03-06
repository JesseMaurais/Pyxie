#!/usr/bin/env python
"""Shows how you can change the text in the window decorator"""

import X11, time
from X11 import display, window, wm

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow(width=800, height=80)
wnd.StoreName('Pyxie - Python X Interface with Extensions')
wnd.MapRaised()
dpy.Flush()

time.sleep(3)

dpy.UnmapWindow(wnd)
dpy.DestroyWindow(wnd)
dpy.Close()

