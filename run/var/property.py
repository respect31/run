import inspect
from .var import Var

#TODO: rename to DescriptorVar?
class PropertyVar(Var):
    
    #Public
    
    def __init__(self, prop):
        self._property = prop
 
    def retrieve(self):
        return self._property.__get__(
            self.meta_module, type(self.meta_module))
    
    @property    
    def meta_docstring(self):
        return str(inspect.getdoc(self._property))