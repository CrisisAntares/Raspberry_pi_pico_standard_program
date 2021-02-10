from machine import Pin


switchpin = Pin(0,Pin.IN) #if you use GP0
led = Pin(25, Pin.OUT)#if you use LED in pico

while True:
    if switchpin.value() == 1:# If you push switch
        led.value(1)  # The LED glows.
        print("Yes")
    else:
        led.value(0)  # Low
        print("No")

