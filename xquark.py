import X11
from X11 import display, rm

dpy = X11.Open()

q = rm.StringToQuark(dpy.resource)

s = rm.QuarkToString(q)

print 'Quark', q.value
print s

dpy.Close()

