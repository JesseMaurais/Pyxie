#!/usr/bin/env python
import X11
from X11 import display, window, atom

dpy = X11.Open()
wnd = dpy.root.CreateWindow()


#Specify a window property with an atomic type
wnd.text = X11.Window.Property(dpy.STRING)

#We can now set the property value
wnd.text = 'This text is stored to and fetched from the server.'

#We can also get the property value
print wnd.text

#Deleting the property uses Python's del operator
del wnd.text


dpy.DestroyWindow(wnd)
dpy.Close()

