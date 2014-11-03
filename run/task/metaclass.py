from abc import ABCMeta
from ..helpers import Null
from .prototype import Prototype


class Metaclass(ABCMeta):

    # Public

    def __call__(self, *args, meta_module=Null, meta_updates=None, **kwargs):
        prototype = Prototype(
            *args, meta_class=self, meta_updates=meta_updates, **kwargs)
        if meta_module is Null:
            # Return prototype
            return prototype
        else:
            # Build and return task
            task = prototype.meta_build(meta_module=meta_module)
            return task
