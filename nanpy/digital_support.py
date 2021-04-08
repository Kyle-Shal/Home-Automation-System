from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class digital_support(ArduinoObject):

    def __init__(self, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new')

    @arduinoobjectmethod
    def speakerPlayNote(self, f, port, seconds):
        pass
 
