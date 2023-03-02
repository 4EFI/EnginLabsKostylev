import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]

number = 8*[0]

GPIO.setup ( dac, GPIO.OUT )

str_bin = bin( 255 )

print( str_bin )

len = len( str_bin )

for i in range( 7, -1, -1 ):
        j = i - 8 + len

        if str_bin[ j ] == 'b':
            break 

        if str_bin[ j ] == '0':
            number[ i ] = 0

        if str_bin[ j ] == '1':
            number[ i ] = 1

print( number )

for i in range(8):
    GPIO.output( dac[i], number[i] )

time.sleep( 10 )

GPIO.cleanup()