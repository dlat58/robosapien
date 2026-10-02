import machine
import time

# rs_commands = Robosapien V1
# rsv2_commands = Robosapien V2
from rsv2_commands import COMMANDS

# Import simple Robosapien helper class
from rs import RS

high5 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
high5.irq(lambda p:doHigh5(p))

rs = RS(15, COMMANDS)

def doHigh5(pin):
    if(pin.value()):
        rs.send_command("ROAR")
        #send_command("SPARE_CHANGE")
        #rs.send_command("HEY_BABY")
 