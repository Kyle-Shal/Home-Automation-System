#import modules
from grove_library import *
from time import sleep

#initializing 
connection = arduinoInit("COM4")
speakerInit(8, connection)
lcdInit(connection)

#Note: lcdPrintString() and lcdClearScreen() functions from grove library were renamed as Print() and Clear() respectively. 
#Functions  
#Main function to prompt user for choices     
def question():
    arduinoDigitalWrite(6, 0)
    lcdSetBackground(255, 255, 255)
    Clear()
    temp=(tempGetCelsius(0))//1
    tempstring= temp,"celsius"
    Print(tempstring)
    moveOnKey=input()
           
    Clear()
    Print("Choose function: ")
    Choice=input()
    Clear()
    Print(Choice)
    sleep(1)
    
    if Choice=="1":
        Clear()
        Print ("Alarm System")
        sleep(1)
        Clear()
        Print("System is Armed")
        SetAlarm()
        
    if Choice=="2":
        Clear()
        Print("Home Automation")
        sleep(1)
        Clear()
        Print("Counter Started")
        sleep(1)
        HomeAutomation()
    else:
        question()
        
    
#Alarm Functions  
def SetAlarm():    
    while True:
        TriggerOne=arduinoDigitalRead(2)
        TriggerTwo=arduinoDigitalRead(4)
        Deactivatebutton=arduinoDigitalRead(5)
        
        if TriggerTwo==1 or TriggerOne==1:
            #chainLEDSetColour(0,255,0,0)
            TriggeredAlarm()
        if Deactivatebutton==1:
            AlarmReset()
        else:
            SetAlarm()
def TriggeredAlarm():    
    FX=[1,0,1,0,1,0,1,0,1,0]
    for i in FX:
        speakerPlayNote(8,1000,1)
        Clear()
        Print("Alert!")
        lcdSetBackground(255,255,255)
        lcdSetBackground(255,0,0)
        arduinoDigitalWrite(3, i)
        
    Clear()
    Print("Enter Reset pin")
    password=input()
    Clear()
    Print(password)
    sleep(1)
    
    if password=="1234":
        Clear()
        lcdSetBackground(0, 255, 255,)        
        Print("Deactivated")
        sleep(2)
        question()
                      
    if password!="1234":
        TriggeredAlarm()
    
def AlarmReset():   
    Clear()
    Print("Enter Reset pin")
    password=input()
    Clear()
    Print(password)
    sleep(1)
    
    if password=="1234":
        Clear()
        lcdSetBackground(0, 255, 255,)        
        Print("Deactivated")
        sleep(2)
        question()
        
        
    if password!="1234":
        AlarmReset()

        
#Counter Functions
def HomeAutomation():
    Clear()    
    Print("Light off,0")
    Count=0
    while Count>=0:
        if Count==0:
            arduinoDigitalWrite(6, 0)
            Clear()
            Print("Lights off")
        if Count>0:
            arduinoDigitalWrite(6, 1)
        
        if arduinoDigitalRead(2)==1:
            Count=Count+1
            Clear()
            CountText="Light on,",Count
            Print(CountText)
        if arduinoDigitalRead(4)==1:
            Count=Count-1
            Clear()
            CountText="Light on,",Count
            Print(CountText)
        if arduinoDigitalRead(5)==1:
            Clear()
            Print("Counter Stopped")
            sleep(1)
            arduinoDigitalWrite(6, 0)
            Clear()
            Print("Lights off")
            question()
            
        sleep(1.5)
        
    return



while True:
    question()
