from machine import Pin
from mfrc522 import MFRC522
import utime

reader = MFRC522(spi_id=0,sck=18,miso=19,mosi=23,cs=5,rst=4)
led = Pin(2,Pin.OUT)

print("Bring TAG closer...")
print("")

try:
    while True:
        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card = int.from_bytes(bytes(uid),"little",False)
                #Applications
                if card == 497334785:
                    print("CARD ID: "+str(card)+" \r\nLED on")
                    led.value(1)
                else:
                    print("CARD ID: "+str(card)+" \r\nUNKNOW CARD! \r\nLED off")
                    led.value(0)
        utime.sleep_ms(100) 
except KeyboardInterrupt:
    print("Bye")