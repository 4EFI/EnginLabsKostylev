
import RPi.GPIO as GPIO
import time
import pygame

def dec2bin( value ):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc( dac, comp ):

    for i in range( 256 ):
        GPIO.output( dac, dec2bin( i ) )
        time.sleep(0.0005)
        val = GPIO.input( comp )

        if val == 0:
            return i

        
    return 255

GPIO.setmode( GPIO.BCM )

dac    = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
comp   = 4 
troyka = 17

GPIO.setup ( dac,    GPIO.OUT )
GPIO.setup ( troyka, GPIO.OUT, initial = 1 )
GPIO.setup ( comp,   GPIO.IN )

try:
    start = time.time()
    file  = open( "data.txt", "w" )

    dt = 0.1

    v = []

    while( True ):
        dt_curr = time.time() - start
        if( dt_curr >= dt ):
            start = time.time()
            v.append( adc( dac, comp ) / 256.0 * 3.3 )
            print( "Voltage is", "{:.3f}".format(adc( dac, comp ) / 256.0 * 3.3, 3) )

except KeyboardInterrupt:
    print( "\nZachem menia prerval?? AA?" ) 

finally:
    GPIO.output( dac, 0 )
    GPIO.cleanup()

    


