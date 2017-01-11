# Add Libraries to script

import os
import subprocess
import RPi.GPIO as GPIO
import time

# Add sound section

sounds = ['siren.wav','siren.wav']

print sounds[0]
print sounds[1]
s1_count = 0

# Include BCM I/O pins into python script and define pin numbers

GPIO.setmode(GPIO.BCM)
pbswitch_pin = 18
LED_pinR = 17
LED_pinG = 22
LED_pinB = 24

#Create pbswitch pin as an active low switch (use RPi internal pullup resistor)
#Define LED pin as an output

GPIO.setup(pbswitch_pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_pinR, GPIO.OUT)
GPIO.setup(LED_pinG, GPIO.OUT)
GPIO.setup(LED_pinB, GPIO.OUT)

#Define and set (initialize) the LED output state as False

LED_state = False
def lights_off():
    GPIO.output(LED_pinR, GPIO.LOW)
    GPIO.output(LED_pinG, GPIO.LOW)
    GPIO.output(LED_pinB, GPIO.LOW)


# pbswitch event monitoring loop: check pbswitch_pin and flashes LED output based on new input event being False

lights_off()

while True:
        
	#lights_off()
    new_input_event = GPIO.input(pbswitch_pin)
    if new_input_event == False:
        p = subprocess.Popen(["omxplayer", "-o", "local", sounds[s1_count]])
        s1_count += 1
        if s1_count >= len(sounds):
            s1_count = 0
        # Use p.poll() if you need a return value
        for x in range(1,15):
            LED_state = not LED_state
            GPIO.output(LED_pinR, GPIO.HIGH)
            GPIO.output(LED_pinG, GPIO.LOW)
            GPIO.output(LED_pinB, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED_pinR, GPIO.LOW)
            GPIO.output(LED_pinG, GPIO.HIGH)
            GPIO.output(LED_pinB, GPIO.LOW)
            time.sleep(0.1)
        lights_off()
        p.terminate()  # this kills the sound when the lights are finished
        