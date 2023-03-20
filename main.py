from machine import Pin, PWM
import utime

MID = 1500000
MIN = 890000
MAX = 2300000
DIF = 800000/5
time = 86400

pwm = PWM(Pin(15))
pwm.freq(50)
#pwm.duty_ns(MID)


from machine import Pin
led = Pin(25, Pin.OUT)

led.toggle()
utime.sleep(10)
led.toggle()

while True:
    pwm.duty_ns(890000)
    utime.sleep(time)
    pwm.duty_ns(int(890000 + DIF))
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 2)+70000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 3)+70000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 4)+30000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 5)+30000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 6)+90000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 7)+90000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 8)+90000)
    utime.sleep(time)

    pwm.duty_ns(int(MIN + DIF * 7)+90000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 6)+90000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 5)+30000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 4)+30000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 3)+70000)
    utime.sleep(time)
    pwm.duty_ns(int(MIN + DIF * 2)+70000)
    utime.sleep(time)
    pwm.duty_ns(int(890000 + DIF))
    utime.sleep(time)
