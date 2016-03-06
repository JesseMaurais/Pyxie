import X11 as X

X.Display.connection_number = X.extern_property('XConnectionNumber')

X.Display.string = X.extern_property('XDisplayString', X.String)

X.Display.vendor = X.extern_property('XServerVendor', X.String)

X.Display.version = X.extern_property('XProtocolVersion')

X.Display.revision = X.extern_property('XProtocolRevision')

X.Display.release = X.extern_property('XVendorRelease')

X.Display.root = X.extern_property('XDefaultRootWindow', X.Window)

X.Display.screen_count = X.extern_property('XScreenCount')

X.Display.default_screen = X.extern_property('XDefaultScreen')

X.Display.screen = X.extern_property('XDefaultScreenOfDisplay', X.Screen)

X.Display.resource = X.extern_property('XResourceManagerString', X.String)

X.Display.bitmap_unit = X.extern_property('XBitmapUnit')

X.Display.bitmap_pad = X.extern_property('XBitmapPad')

X.Display.bitmap_bit_order = X.extern_property('XBitmapBitOrder')

X.Display.image_byte_order = X.extern_property('XImageByteOrder')

X.Display.next_request = X.extern_property('XNextRequest')

X.Display.last_request = X.extern_property('XLastKnownRequestProcessed')

X.Display.queue_length = X.extern_property('XQLength')

X.Display.max_request_size = X.extern_property('XMaxRequestSize')

X.Display.ext_max_request_size = X.extern_property('XExtendedMaxRequestSize')

X.Display.motion_buffer_size = X.extern_property('XDisplayMotionBufferSize')


