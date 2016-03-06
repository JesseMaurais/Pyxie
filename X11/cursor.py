import X11 as X, bit

Font = bit.enum(
	"""
	X_cursor
	arrow
	based_arrow_down
	based_arrow_up
	boat
	bogosity
	bottom_left_corner
	bottom_right_corner
	bottom_side
	bottom_tee
	box_spiral
	center_ptr
	circle
	clock
	coffee_mug
	cross
	cross_reverse
	crosshair
	diamond_cross
	dot
	dotbox
	double_arrow
	draft_large
	draft_small
	draped_box
	exchange
	fleur
	gobbler
	gumby
	hand1
	hand2
	heart
	icon
	iron_cross
	left_ptr
	left_side
	left_tee
	leftbutton
	ll_angle
	lr_angle
	man
	middlebutton
	mouse
	pencil
	pirate
	plus
	question_arrow
	right_ptr
	right_side
	right_tee
	rightbutton
	rtl_logo
	sailboat
	sb_down_arrow
	sb_h_double_arrow
	sb_left_arrow
	sb_right_arrow
	sb_up_arrow
	sb_v_double_arrow
	shuttle
	sizing
	spider
	spraycan
	star
	target
	tcross
	top_left_arrow
	top_left_corner
	top_right_corner
	top_side
	top_tee
	trek
	ul_angle
	umbrella
	ur_angle
	watch
	xterm
	"""
	,i=2)


### Methods ###################################################


X.Display.CreatePixmapCursor = X.Callable(
	'XCreatePixmapCursor', X.Cursor,
	['self', X.Display],
	['source_pixmap', X.Pixmap],
	['mask_pixmap', X.Pixmap],
	['foreground', X.ByRef(X.Color)],
	['background', X.ByRef(X.Color)],
	['x', X.Integer],
	['y', X.Integer]
	)
	
X.Display.CreateGlyphCursor = X.Callable(
	'XCreateGlyphCursor', X.Cursor,
	['self', X.Display],
	['source_font', X.Font],
	['mask_font', X.Font],
	['source_char', X.Integer],
	['mask_char', X.Integer],
	['foreground', X.ByRef(X.Color)],
	['background', X.ByRef(X.Color)]
	)
	
X.Display.CreateFontCursor = X.Callable(
	'XCreateFontCursor', X.Cursor,
	['self', X.Display],
	['shape', X.Cardinal, Font.X_cursor]
	)
	
X.Display.FreeCursor = X.Callable(
	'XFreeCursor', int,
	['self', X.Display],
	['cursor', X.Cursor]
	)

X.Display.DefineCursor = X.Callable(
	'XDefineCursor', int,
	['self', X.Display],
	['window', X.Window],
	['cursor', X.Cursor]
	)
	
X.Display.UndefineCursor = X.Callable(
	'XUndefineCursor', int,
	['self', X.Display],
	['window', X.Window]
	)
	
X.Display.RecolorCursor = X.Callable(
	'XRecolorCursor', int,
	['self', X.Display],
	['cursor', X.Cursor],
	['foreground', X.ByRef(X.Color)],
	['background', X.ByRef(X.Color)]
	)

X.Display.QueryBestCursor = X.Callable(
	'XQueryBestCursor', X.Status,
	['self', X.Display],
	['drawable', X.Drawable],
	['width', X.Integer],
	['height', X.Integer],
	['return_width', X.INT],
	['return_height', X.INT]
	)

