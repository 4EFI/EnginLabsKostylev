
import RPi.GPIO as GPIO
import time

def dec2bin( value ):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

GPIO.setmode( GPIO.BCM )

dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]

GPIO.setup ( dac, GPIO.OUT )

try:
    T = int( input() )
    T /= 2**len(dac)
    while( True ):
        for i in range( 0, 256 ):
            time.sleep(T)
            GPIO.output( dac, dec2bin( i ) )

        for i in range( 255, -1, -1 ):
            time.sleep(T)
            GPIO.output( dac, dec2bin( i ) )

except KeyboardInterrupt:
    print( "\nZachem menia prerval?? AA?" ) 

finally:
    GPIO.output( dac, 0 )
    GPIO.cleanup()

    