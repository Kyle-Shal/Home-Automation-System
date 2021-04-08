from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class ChainableLED(ArduinoObject):

    cfg_h_name = 'USE_ChainableLED'

    def __init__(self, pin, count, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', pin, count)

    @arduinoobjectmethod
    def begin(self, pin):
        pass

    @arduinoobjectmethod
    def setRGB(self, led, red, blue, green):
        pass

