from run import Module, InputVar, require, trigger

class MainModule(Module):
    
    #Tasks
    
    def ready(self):
        print('Your choice is "{greeting}".\n'
              'We\'re ready.'.format(
            greeting=self.greeting,))    
    
    @require('ready')
    @trigger('done')
    def greet(self, person='World'):
        """Greet the given person."""
        print('{greeting} {person}!'.format(
            greeting=self.greeting, 
            person=person))
        
    def done(self):
        print('OK. We\'re done.')
        
    #Vars
    
    greeting = InputVar(
        prompt='Type your greeting',
        default='Hello',
    )