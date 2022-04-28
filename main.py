import machine
from machine import Pin
import time


TIMEOUT = 10000
#pulse read pins are on GP26, GP22, gp20 and GP18.
# touch out is on pin GP16 (1M resistor from pulse send pin)
# outPin = Pin(16, Pin.OUT)
oneTick = 100
led = Pin(25, Pin.OUT)
led.off()
p0 = touchPin(26, TIMEOUT) 
p1 = touchPin(22, TIMEOUT) 
p2 = touchPin(20, TIMEOUT) 
p3 = touchPin(18, TIMEOUT) 
pinses = [p0, p1, p2, p3]

def reportStatus(l):
    """ reads list of touchPins and reports which are being touchded """
    m = []
    for p in l:
        n = p.checkPin() 
        m.append(n)
        # time.sleep_ms(10)
    return m

def blinkLed(pin, timeout):
    pin.on()
    time.sleep_ms(timeout)
    pin.off()
    time.sleep_ms(timeout)
            
while True:
    l = reportStatus(pinses)
    if (l[0]>0):
        blinkLed(led, oneTick)
    elif (l[3]>0):
        blinkLed(led, oneTick*2)
    else:
        time.sleep_ms(oneTick)
    print(l)
    # if (l != []):
    #     for p in l:
    #         print(p)
    # else:
    #     pass