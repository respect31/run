import inspect
from ..attribute import AttributeBuilder, AttributeMetaclass, Attribute
from ..task import MethodTask
from ..var import ValueVar, DescriptorVar
from .builder import ModuleBuilder

class ModuleMetaclass(AttributeMetaclass):
     
    #Public
     
    def __new__(cls, name, bases, attrs):
        for key, attr in attrs.items():
            if key.isupper():
                continue
            if key.startswith('_'):
                continue
            if key.startswith('meta_'):
                continue
            if isinstance(attr, type):
                continue
            if isinstance(attr, cls._attribute_class):
                continue
            if isinstance(attr, cls._attribute_builder_class):
                continue
            if getattr(attr, '__isabstractmethod__', False):
                continue   
            if callable(attr):
                attrs[key] = cls._method_task_class(attr)
            elif inspect.isdatadescriptor(attr):
                attrs[key] = cls._descriptor_var_class(attr)
            else:
                attrs[key] = cls._value_var_class(attr)
        return super().__new__(cls, name, bases, attrs)
    
    #Protected
    
    _builder_class = ModuleBuilder
    _attribute_class = Attribute
    _attribute_builder_class = AttributeBuilder
    _method_task_class = MethodTask
    _descriptor_var_class = DescriptorVar
    _value_var_class = ValueVar