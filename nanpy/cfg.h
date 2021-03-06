#pragma once

#define BAUDRATE 9600

// info about existence of other features
#define USE_Info                                    1

// definitions: MCU type, frequency, Arduino version,
// EEPROM size, RAM size, pin count, build time,..
#define USE_Define                                  1

// low level mapping of pins and ports
#define USE_ArduinoCore                             1

// read, write RAM
#define USE_RAM                                     1

// read, write EEPROM
#define USE_EEPROM                                  1

// read, write AVR registers
#define USE_Register                                0

// watchdog and reset
#define USE_Watchdog                                0

#define USE_Tone                                    1

#define USE_LiquidCrystal                           0

// I2C
#define USE_Wire                                    0

#define USE_Servo                                   1

#define USE_Stepper                                 0

// frequency counter,  USE_Tone should be off!
#define USE_Counter                                 0

// external libraries should be installed for the following features:
#define USE_OneWire                                 0
#define USE_DallasTemperature                       0
#define USE_CapacitiveSensor                        0

// https://github.com/adafruit/DHT-sensor-library
#define USE_DHT                                     0

// https://bitbucket.org/fmalpartida/new-liquidcrystal
#define USE_LiquidCrystal_I2C                       0

// https://www.adafruit.com/products/1429
#define USE_TLC5947                                 0

//Grove Components
#define USE_rgb_lcd		                      1
#define USE_digital_support                           1
//#define USE_ultrasonic_distance                       1
//#define USE_rgba_leds				            0
//#define USE_led_bar				      1
#define USE_Grove_LED_Bar              1
#define USE_lcd_display                               1
#define USE_Grove_Ultrasonic			      1
#define USE_ChainableLED                            1
