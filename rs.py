# This class was geneated by AI
# note AI did not modulate the carrier so had to be modified
import time, machine

# This class will control Robosapien V1 or V2
# but requires a dictionary of command values to send
class RS:
    # Initialise everything we need to send commands to Robosapien
    def __init__(self, pin, commands, carrier=39200, t=833, duty=0.3):
        self.commands = commands # a dictionary lookup of names to values
        self.command_bits = commands["BIT_COUNT"] # 8 for V1, 12 for V2
        self.T = t # T is the base period of around 1/1200s
        self.duty_u16 = int(0xFFFF * duty) # Sweet spot is around 30%
        self.pwm = machine.PWM(machine.Pin(pin), freq=carrier)
        self.carrier_off() # Begin with no carrier

    # Turn the carrier on for a period (note it won't turn off again)
    def carrier_on(self, period=0):
        self.pwm.duty_u16(self.duty_u16)
        time.sleep_us(self.T * period)

    # Turn the carrier off for a period (note it won't turn on again)
    def carrier_off(self, period=0):
        self.pwm.duty_u16(0)
        time.sleep_us(self.T * period)

    # Sends a single N-bit command byte to the Robot
    def send_command(self, cmd_str):
        cmd_word = self.commands[cmd_str]
        
        print("Sending {cmd_str} {bits} bit {value:X} command...".format(cmd_str=cmd_str, bits=self.command_bits, value=cmd_word))

        # Switch carrier on for period of 8T
        # This let's robot know we are about to send a command
        self.carrier_on(8)
        
        # Transmit N bits (MSB first)
        for i in range(self.command_bits-1, -1, -1):
            # Extract each bit from the word
            bit = (cmd_word >> i) & 1
            
            if not bit:
                # Low = carrier OFF for 1T, then Carrier ON for 1T
                self.carrier_off(1)
                self.carrier_on(1)
            else:
                # High = carrier OFF for 4T, then Carrier ON for 1T
                self.carrier_off(4)
                self.carrier_on(1)
                
        # Shut down carrier after sending command
        self.carrier_off()
        
        # Give robot a chance to process
        time.sleep_ms(100)