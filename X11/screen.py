import X11 as X

X.Screen.root = X.extern_property('XRootWindowOfScreen', X.Window)

X.Screen.visual = X.extern_property('XDefaultVisualOfScreen', X.Visual)

X.Screen.gc = X.extern_property('XDefaultGCOfScreen', X.GC)

X.Screen.black = X.extern_property('XBlackPixelOfScreen', X.Pixel)

X.Screen.white = X.extern_property('XWhitePixelOfScreen', X.Pixel)

X.Screen.colormap = X.extern_property('XDefaultColormapOfScreen', X.Colormap)

X.Screen.display = X.extern_property('XDisplayOfScreen', X.Display)

X.Screen.number = X.extern_property('XScreenNumberOfScreen')

X.Screen.resource = X.extern_property('XScreenResourceString', X.STRING8)

X.Screen.cells = X.extern_property('XCellsOfScreen')

X.Screen.depth = X.extern_property('XDefaultDepthOfScreen')

X.Screen.does_backing_store = X.extern_property('XDoesBackingStore', bool)

X.Screen.does_save_unders = X.extern_property('XDoesSaveUnders', bool)

X.Screen.width = X.extern_property('XWidthOfScreen')

X.Screen.height = X.extern_property('XHeightOfScreen')

X.Screen.width_mm = X.extern_property('XWidthMMOfScreen')

X.Screen.height_mm = X.extern_property('XHeightMMOfScreen')

X.Screen.max_maps = X.extern_property('XMaxCmapsOfScreen')

X.Screen.min_maps = X.extern_property('XMinCmapsOfScreen')

X.Screen.planes = X.extern_property('XPlanesOfScreen')

X.Screen.event_mask = X.extern_property('XEventMaskOfScreen', X.Bitmask)

