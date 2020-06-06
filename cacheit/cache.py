from functools import partial, wraps

from cachetools import TTLCache, cached
from cachetools.keys import hashkey


def cache(cache):
    def wrapper(func):
        func_name = func.__name__
        name = f'{__file__}:{func_name}'
        
        @cached(cache, key=partial(hashkey, name))
        @wraps(func)
        def new_func(*a, **kw):
            return func(*a, **kw)
        return new_func
    return wrapper
