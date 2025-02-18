from gpiozero import LED
import struct
import serial

ser = serial.Serial("/dev/serial2", 115200, timeout=1)

class Receiver:
    pin_leds = [17, 27, 22, 23]
    leds = {}
    threshold_on = 1502
    threshold_off = 1498
    channel_values = []

    @classmethod
    def setup_leds(cls):
        for pin in cls.pin_leds:
            cls.leds[pin] = LED(pin)
    
    @staticmethod
    def control_leds():
        for key, pin in enumerate(Receiver.pin_leds):
            led = Receiver.leds[pin]
            value = Receiver.channel_values[key]
            
            if value > Receiver.threshold_on:
                led.on()
            elif value < Receiver.threshold_off:
                led.off()
    
    @classmethod
    def read_ibus(cls):
        cls.setup_leds()
        
        while True:
            if ser.in_waiting >= 32:
                data = ser.read(32)
                
                if data[0] == 0x20 and data[1] == 0x40:
                    cls.channel_values = struct.unpack('<14H', data[2:30])
                
                cls.control_leds()

Receiver.read_ibus()