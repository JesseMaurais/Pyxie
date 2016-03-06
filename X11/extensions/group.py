import X11 as X
from X11.extensions.ext import Callable

class Group(X.ID):
	pass
	
X.Display.CreateEmbeddedApplicationGroup = Callable(
	'XagCreateEmbeddedApplicationGroup', X.Status,
	['self', X.Display],
	['visualid', X.VisualID],
	['default_colormap', X.Colormap],
	['black_pixel', X.Pixel],
	['white_pixel', X.Pixel],
	['return_group', Group]
	)
	
X.Display.CreateNonembeddedApplicationGroup = Callable(
	'XagCreateNonembeddedApplicationGroup', X.Status,
	['self', X.Display],
	['return_group', Group]
	)
	
X.Display.DestroyApplicationGroup = Callable(
	'XagDestroyApplicationGroup', X.Status,
	['self', X.Display],
	['group', Group]
	)
	
X.Display.QueryApplicationGroup = Callable(
	'XagQueryApplicationGroup', X.Status,
	['self', X.Display],
	['resource', X.ID],
	['return_group', Group]
	)
	
X.Display.CreateAssociation = Callable(
	'XagCreateAssociation', X.Status,
	['self', X.Display],
	['return_window', X.Window],
	['system_window', X.Pointer]
	)
	
X.Display.DestroyAssociation = Callable(
	'XagDestroyAssociation', X.Status,
	['self', X.Display],
	['window', X.Window]
	)
	
