import machine
from machine import Pin
import time

TIMEOUT = 10000
#pulse read pins are on GP26, GP22, gp20 and GP18.
# touch out is on pin GP16 (1M resistor from pulse send pin)
outPin = Pin(16, Pin.OUT)
p0 = touchPin(Pin(26, Pin.IN), outPin, TIMEOUT, 1) 
p1 = touchPin(Pin(22, Pin.IN), outPin, TIMEOUT, 2) 
p2 = touchPin(Pin(20, Pin.IN), outPin, TIMEOUT, 3) 
p3 = touchPin(Pin(18, Pin.IN), outPin, TIMEOUT, 4) 
pinses = [p0, p1, p2, p3]

def reportStatus(l):
    """ reads list of touchPins and reports which are being touchded """
    m = []
    for p in l:
        n = p.checkPin() 
        if n>0:
            m.append(n)
        time.sleep_ms(10)
    return m
            

while True:
    l = reportStatus(pinses)
    if (l != []):
        for p in l:
            print(p)
    else:
        pass
    time.sleep_ms(25)