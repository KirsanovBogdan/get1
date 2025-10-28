import smbus
from time import sleep
import time


class mcp3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные:{data}, Старший байт: {upper_data_byte:x}, Млдаший байт: {lower_data_byte:x}, Число: {number}")
        return number
    def get_voltage(self):
        return self.dynamic_range * self.get_number() / 1024


if __name__ == "__main__":
    mcp = mcp3021(5.20, verbose = True)
    try:
        while True:
            print(f"Напряжение: {mcp.get_voltage():.3f} B")
            sleep(0.25)
    except KeyboardInterrupt:
        print("\nThe program was stopped by the keyboard")
    finally:
        mcp.deinit()