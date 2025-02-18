import pyvisa
import time

rm = pyvisa.ResourceManager()
signal_generator = rm.open_resource("ASRL6::INSTR", baud_rate=115200, data_bits=8)
print(rm.list_resources())

signal_generator.write("*RST")
for freq in range(100, 202):
    signal_generator.write(f"FREQ {freq} MHz")
    time.sleep(0.5)

signal_generator.close()