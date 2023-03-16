
import RPi.GPIO as GPIO

def dec2bin( value ):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

GPIO.setmode( GPIO.BCM )

dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]

GPIO.setup ( dac, GPIO.OUT )

try:
    while( True ):
        num_str = input()

        if( num_str == "q" ):
            print( "Bye :)" )
            break
        elif( not num_str.isnumeric() ):
            print( "Enter not string..." )
            continue

        num = int( num_str )

        if( num < 0 ): 
            print( "Enter the number >= 0..." )
            continue
        elif( num > 255 ):
            print( "Enter the number <= 255..." )
            continue

        GPIO.output( dac, dec2bin( num ) )
        print( "Voltage is", "{:.3f}".format(num/255*5, 3) )

except KeyboardInterrupt:
    print( "\nZachem menia prerval?? AA?" ) 

finally:
    GPIO.output( dac, 0 )
    GPIO.cleanup()

    


