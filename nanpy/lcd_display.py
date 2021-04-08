from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class lcd_display(ArduinoObject):

    def __init__(self, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new')

    @arduinoobjectmethod
    def lcdInit(self):
        pass

    @arduinoobjectmethod
    def lcdClear(self):
        pass

    @arduinoobjectmethod
    def lcdPrint(self, value):
        pass

    @arduinoobjectmethod
    def lcdMoveCursor(self, x, y):
        pass

