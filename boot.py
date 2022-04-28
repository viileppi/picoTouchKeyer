""" use GP4 to read and GP0 to write, connect these with a megaohm resistor """
import machine
import time

class touchPin:
    """ a capacitive touch circuit """
    def __init__(self, pin, timeOut):
        """ takes a Pin number as input,
            sends a pulse from pin to gnd. if pulse is 
            gone before
            timeout, returns id (which should be int>0)
            else returns -1 or -2
            timeOut is in microseconds 
            initial timeout is 1000000us """
        self.id = pin
        self.pin = Pin(self.id, Pin.OUT)
        self.pin.off()
        self.timeOut = timeOut
        self.pulse_level = 1    # 1 for reading high pulse, 0 for low

    def checkPin(self):
        self.pin.off()
        self.pin.on()
        self.pin = Pin(self.id, Pin.IN) 
        ptime = machine.time_pulse_us(self.pin, self.pulse_level, self.timeOut)
        self.pin = Pin(self.id, Pin.OUT)
        self.pin.off()
        return ptime
        # if ptime < 0:
        #     return ptime
        # else:
        #     return self.id

