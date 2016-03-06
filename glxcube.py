#!/usr/bin/env python

import X11, OpenGL as GL
from X11.extensions import GLX
from OpenGL import utility as GLU


GL.require('GL_VERSION_1_0')
GLX.require('GLX_VERSION_1_0')

import X11.display, X11.window, X11.event


attributes = (X11.Integer*5)(GLX.RGBA, GLX.DOUBLEBUFFER, GLX.DEPTH_SIZE, 16, 0)

display = X11.Open()
screen = display.default_screen
root = display.root


info = GLX.ChooseVisual(display, screen, attributes)
context = GLX.CreateContext(display, info, None, True)

window = root.CreateSimpleWindow(width=640, height=400)
window.SelectInput(X11.event.Mask.StructureNotify)

GLX.MakeCurrent(display, window, context)
window.MapRaised()

GL.Enable(GL.DEPTH_TEST)
GL.ShadeModel(GL.SMOOTH)


theta = 0
quit = False
while not quit:
	theta += 1
	
	GL.Clear(GL.COLOR_BUFFER_BIT | GL.DEPTH_BUFFER_BIT)

	GL.LoadIdentity()
	GLU.LookAt(0,0,-7, 0,0,0, 0,1,0)
	GL.Rotated(theta, 1.0, 0.0, 0.9)

	GL.Begin(GL.QUADS)
	GL.Color3d(0,1,0)	#top
	GL.Vertex3d(+1,+1,-1)
	GL.Vertex3d(-1,+1,-1)
	GL.Vertex3d(-1,+1,+1)
	GL.Vertex3d(+1,+1,+1)
	GL.Color3d(0,0,1)	#bottom
	GL.Vertex3d(+1,-1,+1)
	GL.Vertex3d(-1,-1,+1)
	GL.Vertex3d(-1,-1,-1)
	GL.Vertex3d(+1,-1,-1)
	GL.Color3d(1,0,0)	#front
	GL.Vertex3d(+1,+1,+1) 
	GL.Vertex3d(-1,+1,+1)
	GL.Vertex3d(-1,-1,+1)
	GL.Vertex3d(+1,-1,+1)
	GL.Color3d(1,1,0)	#back
	GL.Vertex3d(-1,+1,-1)
	GL.Vertex3d(+1,+1,-1)
	GL.Vertex3d(+1,-1,-1)
	GL.Vertex3d(-1,-1,-1)
	GL.Color3d(1,0,1)	#right
	GL.Vertex3d(+1,+1,-1)
	GL.Vertex3d(+1,+1,+1)
	GL.Vertex3d(+1,-1,+1)
	GL.Vertex3d(+1,-1,-1)
	GL.Color3d(0,1,1)	#left
	GL.Vertex3d(-1,+1,+1)
	GL.Vertex3d(-1,+1,-1)
	GL.Vertex3d(-1,-1,-1)
	GL.Vertex3d(-1,-1,+1)
        GL.End()

	GLX.SwapBuffers(display, window)

	for event in display.events:

		if event.type is X11.event.Type.DestroyNotify:
			quit = True
			break

		if event.type is X11.event.Type.ConfigureNotify:
			e = event.xconfigure

			aspect = float(e.width) / (e.height or 1)

			GL.Viewport(0, 0, e.width, e.height)

			GL.MatrixMode(GL.PROJECTION)
			GL.LoadIdentity()

			GLU.Perspective(45.0, aspect, 0.1, 100.0)

			GL.MatrixMode(GL.MODELVIEW)
			GL.LoadIdentity()


