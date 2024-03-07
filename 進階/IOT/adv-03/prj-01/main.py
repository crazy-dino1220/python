#########################匯入模組#########################
from machine import Pin, PWM
from time import sleep

######################函式與類別定義######################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
#########################宣告與設定#######################
while True:
    for i in range(1023):
        led.duty(i)
        sleep(0.002)
    for i in range(1023,-1,-1):
        led.duty(i)
        sleep(0.002)
        

#########################主程式###########################
