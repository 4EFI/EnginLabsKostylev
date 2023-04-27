
import RPi.GPIO as GPIO
import time

def dec2bin( value ):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc( dac, comp ):
    bin = 0

    for i in range(7, -1, -1):
        bin += (1 << i)
        GPIO.output( dac, dec2bin( bin ) )
        time.sleep(0.0007)
        val = GPIO.input( comp )
        
        if val == 0:
            bin -= (1 << i)
    
    return bin

def make_arr( t_arr, v_arr, t_start, v_min = -1, v_max = -1 ):
    start = time.time()
    dt    = 0

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
    
    return k + dt

GPIO.setmode( GPIO.BCM )

dac    = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
comp   = 4 
troyka = 17

GPIO.setup ( dac,    GPIO.OUT )
GPIO.setup ( troyka, GPIO.OUT, initial = 1 )
GPIO.setup ( comp,   GPIO.IN )

try:
    file = open( "data.txt", "w" )

    v1_arr = []
    t1_arr = []

    st = time.time()

    print( "Pognali zaregat itot condensator!" )

    t = make_arr( t1_arr, v1_arr, 0, -1, 3.11 )    
    
    for i in range( len( v1_arr ) ):
        file.write( "{:.5f}\n".format( v1_arr[i], 3 ) )

    print( "Razriadka!" )

    GPIO.output( troyka, 0 )

    v2_arr = []
    t2_arr = []
    
    make_arr( t2_arr, v2_arr, t, 0.15, -1 )

    print( time.time() - st )

    for i in range( len( v2_arr ) ):
        file.write( "{:.5f}\n".format( v2_arr[i], 3 ) )

    file.close()

except KeyboardInterrupt:
    print( "\nZachem menia prerval?? AA?" ) 

finally:
    GPIO.output( dac, 0 )
    GPIO.cleanup()

    


