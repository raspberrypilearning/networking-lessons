# Teacher Setup Instructions: networking lesson 2

For this scheme of work students will need access to:

- A Raspberry Pi
- A keyboard and mouse connected to the RPi
- A monitor connected to the RPi
- Latest NOOBS SD card with Raspbian installed (instructions below)
- An Ethernet cable for each pair of Raspberry Pis
- The `network.py` file
- Four female-to-female header leads
- A 270 ohm resistor
- An LED
- A button (or paperclip or similar)

## Downloading and installing NOOBS

Instructions for best practice on [downloading and installing NOOBS can be read here](http://www.raspberrypi.org/documentation/installation/noobs.md).

## Downloading network.py

1. After booting, log in using the default log in `pi` and password `raspberry`.
1. On the command line type: `wget http://git.io/GHo7cw -O network.py --no-check-certificate`.
1. Type `ls` to check that the file has downloaded.

## Making a class set of SD cards

Once you have completed the steps above, you are able to make a copy of your master SD card and then use that to make a class set.

1. Place your master SD card in a computer or laptop with an SD card reader.
1. On windows use [Win disk 32 imager](http://sourceforge.net/projects/win32diskimager/) to make a copy of an SD card. On MAC OSX you can use the `dd` command or a [dd-gui](http://www.gingerbeardman.com/dd-gui/).
1. Remove the master SD card and keep it safe.
1. Take a fresh SD card and insert it into your computer or laptop.
1. Format the SD card then, using your imaging software, select the image and write it to the card.
1. Repeat the last step for the rest of your cards.

## Introduction to GPIO

If you have not used the GPIO pins on the Raspberry Pi before then please see the [introductory guide] (http://www.raspberrypi.org/documentation/usage/gpio/README.md).
