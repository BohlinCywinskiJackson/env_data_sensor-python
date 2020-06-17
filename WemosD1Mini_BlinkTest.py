# Jon Szczesniak
# Bohlin Cywinski Jackson

# Quick sanity tests on Wemos D1 mini connectivity with Micropython
# Useful to check against that new hardware isn't dead and/or that soldering headers onto the board didn't negatively affect the board's performance.
# You should be able to build then upload with only a USB connection.

# Refer to README at head of repository for HOW to upload the script to the board

from machine import Pin
import time

# Declares that we are talking to the on-board LED (GPIO2 is the same as LED_BUILTIN)
# You could alter this declaration to test out commands to other pinouts.
led = Pin(2, Pin.OUT)

# Quick Serial output
print("Blink that LED!")

while True:
    # The following will create a double-blink followed by a pause on LED.
    # Adjust the delay to check to that various builds are working.
    led(LOW)  # could also use led(0)
    time.sleep_ms(200)
    led(HIGH)  # could also use led(1)
    time.sleep_ms(200)
    led(LOW)
    time.sleep_ms(200)
    led.(HIGH)
    time.sleep(1)
