from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class ultrasonic_distance(ArduinoObject):

    def __init__(self, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new')

    @arduinoobjectmethod
    def ultraInit(self, port):
        pass
 
    @arduinoobjectmethod
    def ultraGetDist(self):
        pass
