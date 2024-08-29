import machine
import utime

pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

def pir_handler(pin):

    for i in range(100):
        print("Motion detected. Intruder alert!")
        led.toggle()
        buzzer.toggle()
        utime.sleep_ms(25)

pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)