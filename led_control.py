from wsgiref.simple_server import make_server
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
led=10
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, True)
but="<form method=\"get\" action=\"/on\"><button type=\"submit\">on fukka</button></form><form method=\"get\" action=\"/off\"><button type=\"submit\">off fukka</button></form>"

def complicated_app(env, start_response):
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

