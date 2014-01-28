import inspect
from .task import Task

class FunctionTask(Task):
    
    #Public

    def __init__(self, function):
        self._function = function
    
    def invoke(self, *args, **kwargs):
        return self._function(*args, **kwargs)
        
    @property
    def meta_signature(self):
        return (self.meta_qualname+
                str(inspect.signature(self._function)))
    
    @property    
    def meta_docstring(self):
        return str(inspect.getdoc(self._function))