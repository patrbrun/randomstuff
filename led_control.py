from wsgiref.simple_server import make_server
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
led=10
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, True)
but="<form method=\"get\" action=\"/on\"><button type=\"submit\">Turn it on :D</button></form><form method=\"get\" action=\"/off\"><button type=\"submit\">Turn it off :(</button></form>"


# Pulse width modulation

    # Blink led every 2 secs
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

p = GPIO.PWM(22, 0.5)
#p.start(100)
#p.ChangeDutyCycle(50)
#input("Press return to stop:")
#p.stop()
#GPIO.cleanup()
# End of pulse width modulation

# Brightless level
#import pigpio
#p = pigpio.pi()
#p.set_PWM_dutycycle(22, 255)
#p.set_PWM_dutycycle(27, 128)
#p.set_PWM_dutycycle(10, 128)
#p.stop()
# End of brightness level

def simple_app(env, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    if env["PATH_INFO"] == "/on":
        print("user asked for /on")
        GPIO.output(led, False)
        return(but)
    elif env["PATH_INFO"] == "/off":
        print("user asked for /off")
        GPIO.output(led, True)
        return(but)
    else:
        GPIO.output(led, True)
        print("user asked for something else")
        return(but)


httpd = make_server("", 8000, simple_app)
print "Serving on port 8000..."
httpd.serve_forever()

