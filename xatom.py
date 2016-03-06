#!/usr/bin/env python
"""Shows how to read properties of a window"""

import X11
from X11 import display, atom

dpy = X11.Open()

#Iterate properties of the root window (there should be alot)
for atom in dpy.root.properties:
	print atom.name

dpy.Close()

