import inspect
from ..task import task
from .descriptor import DescriptorVar


class var(task):
    """Decorate method to make var with default kwargs to invoke.

    Examples
    --------
    There are two ways to use decorator:

    - Form without kwargs is designed for case when you have to convert method
      to var prototype immidiatly in class body to use some of it methods::

        class Module(Module):

            @var
            def method(self):
                pass

            method.Require('other_method')

    - Form with kwargs makes the same and adds default kwargs to invoke::

        class Module(Module):

            @var(**kwargs)
            def method(self, **kwargs):
                pass
    """

    # Public

    def match(self, obj):
        if inspect.isdatadescriptor(obj):
            return True
        if inspect.isfunction(obj):
            return True
        return False

    def make(self, obj):
        descriptor = obj
        if not inspect.isdatadescriptor(obj):
            descriptor = property(obj)
        prototype = DescriptorVar(descriptor, *self.args, **self.kwargs)
        return prototype
