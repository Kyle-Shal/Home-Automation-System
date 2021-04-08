# Author: Mahya Soleimani <m.soleimani.bsn@gmail.com>
# Description: To support rgba_leds
# Dependencies: None

from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class rgba_leds(ArduinoObject):

    def __init__(self, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new')

    @arduinoobjectmethod
    def rgbLedInit(self, digitalPin, count):
        pass

    def rgbLedHSB(self, led, hue, saturation, brightness):
        pass

    @arduinoobjectmethod
    def rgbLedRGB(self, led, red, green, blue):
        pass
