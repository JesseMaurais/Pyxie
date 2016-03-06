#!/usr/bin/env python
import X11
from X11 import display, screen, window, event
from X11.extensions import render

dpy = X11.Open()
fmt = dpy.screen.visual.format
wnd = dpy.root.CreateSimpleWindow()
pic = wnd.CreatePicture(fmt)
col = dpy.RenderColor('Green')

wnd.SelectInput(event.Mask.Exposure)
wnd.MapRaised()

Op = render.PictOp.Src

for e in dpy:
	if e.type is event.Type.Expose:
		Op.CompositeFillRectangle(pic, col, 110, 50, 100, 100)
		
		
### Picture Operations Reference Table ########################################
#
# Formula:	Out.Color = Src.Color * Src.Factor + Dst.Color * Dst.Factor
#
# Color is a channel with red, green, blue, and alpha
# Factor is a scalar determined by the operation (see below)
#
# Operation             Src.Factor              Dst.Factor
#------------------------------------------------------------------------------
# Clear                 0                       0
# Src                   1                       0
# Dst                   0                       1
# Add                   1                       1
# Xor                   1 - Dst.Alpha           1 - Src.Alpha
# Over                  1                       1 - Src.Alpha
# OverReverse           1 - Dst.Alpha           1
# In                    Dst.Alpha               0
# InReverse             0                       Src.Alpha
# Out                   1 - Dst.Alpha           0
# OutReverse            0                       1 - Src.Alpha
# Atop                  Dst.Alpha               1 - Src.Alpha
# AtopReverse           1 - Dst.Alpha           Src.Alpha
#
# For full table goto:
# http://cgit.freedesktop.org/xorg/proto/renderproto/plain/renderproto.txt

