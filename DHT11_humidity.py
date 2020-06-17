# Jon Szczesniak
# Bohlin Cywinski Jackson

# Quick sanity tests on DHT11 temp and humidity module with the Wemos D1 mini with Micropython
# Useful to check against that new hardware isn't dead and/or that soldering headers onto the board didn't negatively affect the board's performance.
# You should be able to build then upload with only a USB connection.

# Refer to README at head of repository for HOW to upload the script to the board

from machine import Pin
import time
# Using the Dallas One-Wire library rather than the Adafruit CircuitPython library
# I believe that the dht library is built-in to micropython
import dht

# Declare Pin 4 as the data input pin
dhtpin = pin(4, Pin.IN)
# dht.DHT11() also states that we are using a DHT11
# we could also assign with dht.DHT22() if we want to use the DHT22 device later
dhtdevice = dht.DHT11(dhtpin)

while True:
    # create the structure for the sensors to fail gracefully
    try:
        # call the device to make measurements
        dhtdevice.measure()

        # read the temp in C
        temp_c = dhtdevice.temperature()
        # convert temp from C to F
        temp_f = temp_c * (9 / 5) + 32
        # read humidity
        humid = dhtdevice.humidity()

        print(
        "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
        temperature_f, temperature_c, humidity
        )

        print(f"Humidity: {humid:.1f} %  |  Temperature: {temp_c:.1f} °C ~ {temp_f:.1f} °F")

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print("Failed to read from DHT sensor.")
        print(f"[ERROR] {error.args[0]}")

    # Sleep 2s between readings
    time.sleep(2.0)
