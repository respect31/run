from copy import copy
from box.collections import merge_dicts
from ..converter import Result
from .update import TaskUpdate


class Prototype(Result):

    # Public

    def __init__(self, *args, meta_class, meta_updates=None, **kwargs):
        if meta_updates is None:
            meta_updates = []
        self.__class = meta_class
        self.__updates = copy(meta_updates)
        self.__args = args
        self.__kwargs = kwargs
        self.__name = None

    def __getattr__(self, name):
        if name.startswith('_'):
            return super().__getattribute__(name)
        if hasattr(self.__class, name):
            attr = getattr(self.__class, name)
            # TODO: more attributes to forward from class?
            if isinstance(attr, type):
                return attr
        self.__name = '.'.join(filter(None, [self.__name, name]))
        return self

    def __setattr__(self, name, value):
        if name.startswith('_'):
            return super().__setattr__(name, value)
        name = '.'.join(filter(None, [self.__name, name]))
        update = TaskUpdate('__setattr__', name, value)
        self.__updates.append(update)
        self.__name = None

    def __call__(self, *args, **kwargs):
        if self.__name is None:
            raise TypeError(
                'Object "{self}" is not callable'.format(self=self))
        update = TaskUpdate(self.__name, *args, **kwargs)
        self.__updates.append(update)
        self.__name = None
        return self

    def __meta_fork__(self, *args, **kwargs):
        # Documented public wrapper in :func:`.fork`
        eupdates = copy(self.__updates)
        eargs = self.__args + args
        ekwargs = merge_dicts(self.__kwargs, kwargs)
        return type(self)(
            *eargs,
            meta_class=self.__class,
            meta_updates=eupdates,
            **ekwargs)

    def __meta_build__(self, module):
        # Documented public wrapper in :func:`.build`
        task = self.__class.__meta_create__(
            *self.__args,
            meta_module=module,
            meta_updates=self.__updates,
            **self.__kwargs)
        if not module:
            # Main module - update
            task.__meta_update__()
        return task
