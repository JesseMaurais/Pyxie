#!/usr/bin/env python
import X11
from X11 import display, screen, window, event, font, graphic, drawable

dpy = X11.Open()
wnd = dpy.root.CreateSimpleWindow()
wnd.SelectInput(event.Mask.Exposure)
wnd.MapRaised()

fnt = dpy.LoadFont('*luxisans-medium-r*')
gc = dpy.screen.gc

# You must attach a font to a graphics context to use it
gc.SetFont(fnt)
# We also need to specify the color we will draw with
gc.SetForeground(dpy.screen.white)

for name in dpy.fonts:
	print name

msg = 'Hello World'

for e in dpy:
	if e.type is event.Type.Expose:
		wnd.DrawString(gc, 55, 89, msg, len(msg))

# Font naming conventions go like this

# -foundry-family-weight-slant-set--pixels-point-horz-vert-space-width-charset

# foundry       Who made the font
# family        The font family/name (sans, serif, etc)
# weight        bold or medium
# slant         r for regular, o for oblique (like italic)
# pixel         Pixel size
# point         Point size
# horz          Horizontal size
# vert          Vertical size
# space         m for monospace, p for proportional
# width         Average width for p, exact width for m
# charset       A cryptic ISO serial number

# Wildcard character * is used to match font names
# Any part you don't care about, fix a wildcard over it

