from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class Grove_LED_Bar(ArduinoObject):

    def __init__(self, pin, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', pin+1, pin, True)

 
    @arduinoobjectmethod
    def setLevel(self, level):
        print(level)
        pass
     

