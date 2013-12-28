import sys
import logging.config
from lib31.program import Program
from lib31.python import cachedproperty
from .cluster import Cluster
from .dispatcher import dispatcher
from .command import Command
from .handler import CallbackHandler
from .settings import settings
from .task import Task, InitiatedTaskSignal, CompletedTaskSignal
from .var import InitiatedVarSignal, RetrievedVarSignal

class Program(Program):
    
    #Public
    
    def __init__(self, argv):
        super().__init__(argv)
        self._stack = []
     
    def __call__(self):
        self._config()
        self._execute()
         
    #Protected
    
    def _config(self):
        self._config_logging()
        self._config_dispatcher()
        
    def _config_logging(self):
        logging.config.dictConfig(settings.logging)
        logger = logging.getLogger()
        if self._command.debug:
            logger.setLevel(logging.DEBUG)
        if self._command.verbose:
            logger.setLevel(logging.INFO)
        if self._command.quiet:
            logger.setLevel(logging.ERROR)      
        
    def _config_dispatcher(self):
        dispatcher.add_handler(CallbackHandler(
            self._on_initiated_attribute, 
            signals=[InitiatedTaskSignal, 
                     InitiatedVarSignal]))
        dispatcher.add_handler(CallbackHandler(
            self._on_executed_attribute, 
            signals=[CompletedTaskSignal, 
                     RetrievedVarSignal])) 
    
    #TODO: refactor
    def _execute(self):
        try:
            for attribute in self._attributes:
                if isinstance(attribute, Task):
                    result = attribute(
                        *self._command.args, **self._command.kwargs)
                    if result:
                        print(result)
                else:
                    print(attribute)
        except Exception:
            import traceback
            info = sys.exc_info()
            lines = traceback.format_exception_only(*info[:2])
            message = ''.join(lines).strip()
            if not self._command.debug:
                self._logger.error(message)
            else:
                self._logger.exception(message)
    
    @cachedproperty
    def _attributes(self):
        attributes = getattr(
            self._cluster, self._command.attribute)
        return attributes
        
    @cachedproperty   
    def _cluster(self):
        return Cluster(
            names=self._command.names,
            tags=self._command.tags,
            path=self._command.path, 
            file_pattern=self._command.file,
            recursively=self._command.recursively,
            existent=self._command.existent)
    
    @cachedproperty
    def _command(self):
        return Command(self._argv)
    
    def _on_initiated_attribute(self, signal):
        if not self._command.stackless:
            self._stack.append(signal.attribute)   

    def _on_executed_attribute(self, signal):
        self._log_executed_attribute(signal.attribute)
        if not self._command.stackless:
            self._stack.pop()
    
    def _log_executed_attribute(self, attribute):
        if self._command.stackless:
            message = attribute.meta_name
        else:
            names = []
            previous = self._stack[0]
            names.append(previous.meta_name)
            for attribute in self._stack[1:]:
                current = attribute
                if current.meta_module == previous.meta_module:
                    names.append(current.meta_attribute_name)
                else:
                    names.append(current.meta_name) 
                previous = current
            message = '/'.join(names)
        logger=logging.getLogger('executed')
        logger.info(message)
     
    @cachedproperty    
    def _logger(self):
        return logging.getLogger(__name__)
    
        
program = Program(sys.argv)