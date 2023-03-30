
import RPi.GPIO as GPIO
import time

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
comp   = 4 
troyka = 17

GPIO.setup ( dac,    GPIO.OUT )
GPIO.setup ( troyka, GPIO.OUT, initial = 1 )
GPIO.setup ( comp,   GPIO.IN )

try:
    while( True ):
        print( "Voltage is", "{:.3f}".format(adc( dac, comp ) / 256.0 * 3.3, 3) )

except KeyboardInterrupt:
    print( "\nZachem menia prerval?? AA?" ) 

finally:
    GPIO.output( dac, 0 )
    GPIO.cleanup()

    


