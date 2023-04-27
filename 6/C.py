
import RPi.GPIO as GPIO
import time

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
    k  = 0

    v_arr = [0]
    t_arr = [0]

    while( True ):
        dt_curr = time.time() - start
        out     = adc( dac, comp )
        v       = out / 256.0 * 3.3

        if( dt_curr >= dt ):
            start = time.time()
            k += dt
            v_arr.append( v )
            t_arr.append( k )

            print( "Voltage is", "{:.3f}".format( v, 3 ) )

        if( v >= 3 ):
            break
    
    for i in range( len( v_arr ) ):
        file.write( "{:.2f} ".format( t_arr[i], 3 ) )
        file.write( "{:.5f}\n".format( v_arr[i], 3 ) )

except KeyboardInterrupt:
    print( "\nZachem menia prerval?? AA?" ) 

finally:
    GPIO.output( dac, 0 )
    GPIO.cleanup()

    


