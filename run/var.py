from abc import ABCMeta, abstractmethod
from .attribute import AssociatedAttribute

class Var(AssociatedAttribute, metaclass=ABCMeta):
    
    #Public

    def __get__(self, namespace, namespace_class=None):
        self.resolve()     
        return self.retrieve()
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
        
class ValueVar(Var):
    
    #Public
    
    def __init__(self, value, **kwargs):
        self._value = value
        super().__init__(**kwargs)
 
    def retrieve(self):
        return self._value
    

class PropertyVar(Var):
    
    #Public
    
    def __init__(self, prop, **kwargs):
        self._property = prop
        super().__init__(**kwargs)
 
    def retrieve(self):
        return self._property.__get__(self.namespace, self.namespace.__class__)  