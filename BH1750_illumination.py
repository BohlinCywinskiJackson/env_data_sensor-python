# Jon Szczesniak
# Bohlin Cywinski Jackson

# Quick sanity tests on BH1750 illumination module with the Wemos D1 mini with Micropython
# Useful to check against that new hardware isn't dead and/or that soldering headers onto the board didn't negatively affect the board's performance.
# You should be able to build then upload with only a USB connection.

# Refer to README at head of repository for HOW to upload the script to the board

import machine
import time
# Micropython BH1750 Library
# https://github.com/PinkInk/upylib/tree/master/bh1750
from bh1750 import BH1750


# Declare the pins that we are going to use for the I2C
# Then set up I2C
scl = machine.Pin(1)  # defines D1 as I2C SCL
sda = machine.Pin(2)  # defines D2 as I2C SDA
i2c = machine.I2C(scl,sda)

s = BH1750(i2c)  # addr defaults to 0x23, or
#s = BH1750(i2c, 0x23)  # specify addr explicitly, or
#s = BH1750(i2c, 0x5c)  # pull ADDR pin high and use alternate i2c address

while True:
    lux = s.luminance(BH1750.CONT_HIRES_1)  # see notes below for reading type
    print(f"Light: {lux} lx")

    time.sleep(1)  # delay for 1s before repeating loop

# Other modes for luminance sensor reading (CONT_HIRES_1 is default)
# CONT_LOWRES	    Continuous, low resolution (4lx), sampling takes ~24ms, sensor remains on after reading.
# CONT_HIRES_1	    Continuous, high resolution (1lx), sampling takes ~180ms, sensor remains on after reading.
# CONT_HIRES_2	    Continuous, very high resolution (.5lx), sampling takes ~180ms, sensor remains on after reading.
# ONCE_HIRES_1      One-shot, low resolution (4lx), sampling takes ~24ms, sensor powered down after reading
# ONCE_HIRES_2      One-shot, high resolution (1lx), sampling takes ~180ms, sensor powered down after reading
# ONCE_LOWRES	    One-shot, very high resolution (.5lx), sampling takes ~180ms, sensor powered down after reading
