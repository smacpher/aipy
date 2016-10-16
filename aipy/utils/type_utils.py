# Utilities for type checking.

def is_function(fn):
    return hasattr(fn, '__call__')

