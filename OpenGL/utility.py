import ctypes
from ctypes.util import find_library

lib = ctypes.CDLL(find_library('GLU'))

from OpenGL import GLdouble

# Needs more work

Ortho2D = lib.gluOrtho2D
Ortho2D.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]

Perspective = lib.gluPerspective
Perspective.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble]

LookAt = lib.gluLookAt
LookAt.argtypes = [GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble]


