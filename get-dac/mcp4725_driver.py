import smbus
class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()
    
    def setnumber(self, number):
        if not isinstance(number, int):
            print("DAC input can only take integer values")
        if not (0 <= number <= 4096):
            print("number out of bit depth of MCP7425 (12bit)")
        
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"number: {number}, data to i2c: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def setvoltage(self, voltage):
        self.setnumber(int(voltage/self.dynamic_range * 4096 - 1))
    
if __name__ == "__main__":
    dac = MCP4725(5.16, 0x61, True)
    try:
        while True:
            try:
                voltage = float(input("input voltage i Volts: "))
                dac.setvoltage(voltage)
            except ValueError:
                print("incorrect input, try again")
    finally:
        dac.deinit()

