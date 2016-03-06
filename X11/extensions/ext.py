import X11 as X

Callable = X.Wrapper('Xext')

# libXext contains several X11 extension entries
# We need to link it only once for all of them
# Other modules will import this Callable

