from AgentFunctions import *
class command:  
    def __init__(self, message):
        self.message = message
        self.function_name, *self.args = message.split()

    def execute(self):
        if self.function_name in FUNCTION_MAPPINGS:
            FUNCTION_MAPPINGS[self.function_name](*self.args)