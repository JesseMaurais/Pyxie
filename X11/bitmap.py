import X11 as X

X.Display.CreatePixmapFromBitmapData = X.Callable(
	'XCreatePixmapFromBitmapData', X.Pixmap,
	['self', X.Display],
	['drawable', X.Drawable],
	['data', X.String],
	['width', X.Integer],
	['height', X.Integer],
	['foreground', X.Pixel],
	['background', X.Pixel],
	['depth', X.Integer]
	)
	
X.Display.CreateBitmapFromData = X.Callable(
	'XCreateBitmapFromData', X.Pixmap,
	['self', X.Display],
	['drawable', X.Drawable],
	['data', X.String],
	['width', X.Integer],
	['height', X.Integer]
	)

X.Display.WriteBitmapFile = X.Callable(
	'XWriteBitmapFile', int,
	['self', X.Display],
	['filename', X.String],
	['bitmap', X.Pixmap],
	['width', X.Integer],
	['height', X.Integer],
	['x_hot', X.Integer],
	['y_hot', X.Integer]
	)
	
X.Display.ReadBitmapFile = X.Callable(
	'XReadBitmapFile', int,
	['self', X.Display],
	['drawable', X.Drawable],
	['filename', X.String],
	['return_width', X.INT32],
	['return_height', X.INT32],
	['return_bitmap', X.Pixmap],
	['return_x_hot', X.INT32],
	['return_y_hot', X.INT32]
	)

ReadFileData = X.Callable(
	'XReadBitmapFileData', int,
	['filename', X.String],
	['return_width', X.INT32],
	['return_height', X.INT32],
	['return_data', X.STRING8],
	['return_x_hot', X.INT32],
	['return_y_hot', X.INT32]
	)

