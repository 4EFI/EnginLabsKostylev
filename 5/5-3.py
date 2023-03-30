
import RPi.GPIO as GPIO
import time
import math

def dec2bin( value ):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]
    
def adc( dac, comp ):
    bin = 0

    for i in range(7, -1, -1):
        bin += (1 << i)
        GPIO.output( dac, dec2bin( bin ) )
        time.sleep(0.0005)
        val = GPIO.input( comp )
        
        if val == 0:
            bin -= (1 << i)
    
    return bin

GPIO.setmode( GPIO.BCM )

dac    = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
leds   = [ 21, 20, 16, 12, 7, 8, 25, 24 ]
comp   = 4 
troyka = 17

GPIO.setup ( dac,    GPIO.OUT )
GPIO.setup ( leds,   GPIO.OUT )
GPIO.setup ( troyka, GPIO.OUT, initial = 1 )
GPIO.setup ( comp,   GPIO.IN )

try:
    while( True ):
        val = int( adc( dac, comp ) )
        u = val / 256.0 * 3.3
        print( "Voltage is", "{:.3f}".format( u, 3) )

        n = math.ceil( val/256*8 )

        bin_num = 8 * [ 0 ]
        for i in range( n ):
            bin_num[i] = 1

        GPIO.output( leds, bin_num )

except KeyboardInterrupt:
    print( "\nZachem menia prerval?? AA?" ) 

finally:
    GPIO.output( dac, 0 )
    GPIO.cleanup()

    


