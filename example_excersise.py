class CacheManager(dict):
    def __init__(self, namespace, cache, app_name):
        self.namespace = namespace
        self.cache = cache
        self.app_name = app_name

    def append(self, tup):
        if isinstance(tup, tuple) and len(tup) == 4:
            return self.__dict__.append(self, tup)
        raise ValueError('CacheKey only takes objects of type: tuple, with (func, ignore_args, args, kwargs)')
    
    def __setitem__(self, key, item): 
        self.__dict__[key] = item

    def __getitem__(self, key): 
        return self.__dict__[key]

    def __repr__(self): 
        return repr(self.__dict__)

    def __len__(self): 
        return len(self.__dict__)

    def __delitem__(self, key): 
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return self.__dict__.has_key(k)

    def pop(self, k, d=None):
        return self.__dict__.pop(k, d)

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict):
        return cmp(self.__dict__, dict)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))


o = CacheManager()
o.foo = "bar"
o['lumberjack'] = 'foo'
o.update({'a': 'b'}, c=44)
print 'lumberjack' in o
print o
