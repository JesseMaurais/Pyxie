#!/usr/bin/env python
import X11
from X11 import display, window, wm

dpy = X11.Open()

root, parent, child, count = dpy.root.QueryTree()

assert root.value == dpy.root.value

for index in range(count):
	print child[index].name

