# Magic button

This is sample code for using a physical button connected to the GPIO port on your RPi.

You need RPi.GPIO for this to work.

If you want to run the example, you also need uinput to map the physical button to a keyboard event.

## Setup

### Prepare Raspian
*Let's assume a basic Raspbian setup installed through NOOBS. (It should work on other systems too, however this is what I used to test this on)*

Run `sudo apt-get update` followed by `sudo apt-get upgrade` to make sure you're running the latest stable releases of all software installed.

### Install RPi.GPIO
RPi.GPIO comes bundled with Raspian now. However, if something goes wrong, it might be an option to install it manually:

You might be able to install RPi.GPIO and all it's dependencies at once using this one command:

`sudo apt-get -y install python-rpi.gpio`

If you run into any problems later on with RPi.GPIO not being installed correctly, explicitly install its dependencies using the line below, then install it again using the line above.

`sudo apt-get install python-smbus ipython bluetooth bluez-utils python-cwiid python-scipy python-numpy python-pygame python-setuptools libsdl-dev`

To make sure it works, create a `test.py` script, import the library `import RPi.GPIO as GPIO` and try running it. GPIO **needs** root permissions so running any of the following code examples has to be run with sudo: `sudo python test.py`

### Optional: install uinput
Installing uinput is easiest through pip. pip doesn't come installed with Raspbian so let's install that first. Download the installation file from Github using `wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py`. When that's done, run `sudo python get-pip.py`.

Downloading uinput on your system is now very easy: `sudo pip install python-uinput`.

However, running scripts that use uinput will throw an **OSError: [Errno 2] No such file or directory** when creating a new uinput.Device.

This is because pip hasn't linked uinput to your device modules yet. You can link them by running `sudo modprobe uinput`. You probably want this happening on boot, so also edit the `/etc/modules`-file and add `uinput` on its own line. This will make sure the device gets properly installed when Raspbian boots.

### Connecting a physical button to the Raspberry Pi GPIO ports
*Coming soon*