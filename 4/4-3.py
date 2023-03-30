
import RPi.GPIO as GPIO

def dec2bin( a ):
    return [int (digit) for digit in bin(a)[2:].zfill(8)]

shim_pin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup( shim_pin, GPIO.OUT )

dac = [26, 13, 19, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
 
pwm = GPIO.PWM(shim_pin, 1000)
pwm.start(0)

try:
    while True:
        duty = int( input() )
        pwm.ChangeDutyCycle(duty)
        
        print( "Voltage: {:.3f}".format(duty * 3.3 / 100) )

except KeyboardInterrupt:
    print( "AAAA" )
        
finally:
    GPIO.output(shim_pin, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()