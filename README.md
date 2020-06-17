# Description

Playing around with python versions of all of the *.ino files that we are creating/testing in the other repository.
These aren't 100% baked, but I'm just trying to learn a bit about micropython as we play with the Arduino code.

## Usage

The following is a quick hit-list of what you need to do to get a to full REPL on the board.
You are going to need to get the latest micropython firmware form the ESP8266 from [here](https://micropython.org/download/esp8266/).
You are also going to want to make sure you have the device plugged in and you know what port it is communicating with the computer on.

```bash
cd <YOUR_DOWNLOAD_FOLDER>
# install esptool
pip install esptool

# Now we want to erase the flash on the board, regardless of what is on there
# the port listed below is the syntax for Mac of Linux
# if you ae Windows, it will be COMx where you get x from the Device Manager
esptool.py --port /path/to/ESP8266 erase_flash
# for window it will likely look like this
esptoolpy --port COM5 erase_flash

# Let's flash the firmware on the device
# replace the *.bin file with whatever you downloaded above
esptool.py --port /path/to/ESP8266 --baud 460800 write_flash --flash_size=detect 0 firmware.bin
```
This may take a few minutes, but the command prompt will lead you along the right path.

Once you have the firmware updated, you need to go and download a program called [puTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/).
This program allows for a serial communication on your computer.
The settings for this are pretty simple:

1. select the radio button called `Serial`
1. enter the assigned port number `COM5` or similar
1. use a baud rate of `115200`
1. hit connect

When you get to the command prompt, you may see some gibberish.
Press the `RST` button the ESP8266 a few times and you'll be greeted with

```bash
>>>
```

Try typing

``` python
print('Hello World')
```

and you are all set!

## Next Steps

I need to figure out a how to load scripts onto the main.py file.
Right now, I'm typing out the lines of code from these files, but I know that's not the most efficient.
