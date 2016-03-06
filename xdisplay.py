#!/usr/bin/env python
"""Tests all the class properties of the foreign objects, display and screen"""

import X11
from X11 import display, screen

dpy = X11.Open()
scn = dpy.screen

# display properties

print dpy.vendor
print 'version %d.%d:%d' % (dpy.version, dpy.revision, dpy.release)

print 'display', dpy.string

print 'max request size', dpy.max_request_size
print 'extended max request size', dpy.ext_max_request_size
print 'motion buffer size', dpy.motion_buffer_size

print 'bitmap unit', dpy.bitmap_unit
print 'bit order', dpy.bitmap_bit_order
print 'byte order', dpy.image_byte_order

print 'screen', dpy.default_screen, 'of', dpy.screen_count

# screen properties

print '%d x %d x %d' % (scn.width, scn.height, scn.depth)
print '%d by %d millimetres' % (scn.width_mm, scn.height_mm)

print 'does backing stores:', scn.does_backing_store
print 'does save unders:', scn.does_save_unders

print 'colormap cells', scn.cells
print 'min %d, max %d, colormaps' % (scn.min_maps, scn.max_maps)

# these relationships hold

assert dpy.value == scn.display.value

assert scn.value == dpy.screen.value

assert dpy.default_screen == scn.number

assert dpy.root.value == scn.root.value

# finish

dpy.Close()

