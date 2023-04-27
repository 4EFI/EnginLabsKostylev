
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

def make_arr( t_arr, v_arr, t_start, v_min = -1, v_max = -1 ):
    start = time.time()
    dt    = 0.1

    k = t_start

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

        if( v_min != -1 ):
            if( v <= v_min ):
                break

        if( v_max != -1 ):
            if( v >= v_max ):
                break
    
    return k

GPIO.setmode( GPIO.BCM )

dac    = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
comp   = 4 
troyka = 17

GPIO.setup ( dac,    GPIO.OUT )
GPIO.setup ( troyka, GPIO.OUT, initial = 1 )
GPIO.setup ( comp,   GPIO.IN )

try:
    file = open( "data.txt", "w" )

    dt = 0.1
    k  = 0

    v1_arr = []
    t1_arr = []

    print( "Pognali zaregat itot condensator!" )

    t = make_arr( t1_arr, v1_arr, 0, -1, 3 )    
    
    for i in range( len( v1_arr ) ):
        file.write( "{:.2f} ".format(  t1_arr[i], 3 ) )
        file.write( "{:.5f}\n".format( v1_arr[i], 3 ) )

    print( "Razriadka!" )

    GPIO.output( troyka, 0 )

    v2_arr = []
    t2_arr = []
    
    print( make_arr( t2_arr, v2_arr, t, 0.2, -1 ) )

    for i in range( len( v2_arr ) ):
        file.write( "{:.2f} ".format(  t2_arr[i], 3 ) )
        file.write( "{:.5f}\n".format( v2_arr[i], 3 ) )

except KeyboardInterrupt:
    print( "\nZachem menia prerval?? AA?" ) 

finally:
    GPIO.output( dac, 0 )
    GPIO.cleanup()

    


