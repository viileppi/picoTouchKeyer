""" use GP4 to read and GP0 to write, connect these with a megaohm resistor """
import machine
import time

class touchPin:
    """ a capacitive touch circuit """
    def __init__(self, pinIn, pinOut, timeOut, id):
        """ takes two Pin objects as input  and output,
            sends a pulse of approximately half the timeout
            from pinOut to pinIn. if pulse is gone before
            timeout, returns id (which should be int>0)
            else returns -1 or -2
            timeOut is in microseconds 
            initial timeout is 1000000us """
        self.touchRead = pinIn
        self.sendPulse = pinOut
        self.timeOut = timeOut
        self.sendPulse.off()
        self.pulse_level = 1    # 1 for reading high pulse, 0 for low
        self.timer = machine.Timer()
        self.id = id

    def checkPin(self):
        self.sendPulse.on()
        ptime = machine.time_pulse_us(self.touchRead, self.pulse_level, self.timeOut)
        self.sendPulse.off()
        if ptime < 0:
            return ptime
        else:
            return self.id