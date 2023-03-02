import RPi.GPIO as GPIO
import time 

def LedBlink( channel, sleepTime ):
    flag = 0
    
    while(  True  ):
        if( flag ):
            flag = 0
    else:
        flag = 1
    
    GPIO.output( channel, flag )

    time.sleep( sleepTime )

GPIO.setmode( GPIO.BCM )

channelIn  = 27
channelOut = 22

GPIO.setup ( channelOut, GPIO.OUT )
GPIO.setup ( channelIn,  GPIO.IN )

flag = GPIO.input( channelIn )

GPIO.output( channelOut, flag )

time.sleep( 10 )

GPIO.cleanup()



