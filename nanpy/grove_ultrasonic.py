from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class Ultrasonic(ArduinoObject):
	cfg_h_name = 'USE_Grove_Ultrasonic'
	
	def __init__(self, pin, connection=None):
		ArduinoObject.__init__(self, connection=connection)
		self.id = self.call('new', pin)
		
	@returns(int)
	@arduinoobjectmethod
	def MeasureInCentimeters(self):
		pass