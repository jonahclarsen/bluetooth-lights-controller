# bluetooth_lights_controller
A modification of [kabyru's modification](https://github.com/kabyru/govee-btled-controller) of [Christian Volkmann's govee_btled wrapper](https://github.com/chvolkmann/govee_btled), fixing a bug with multiple lights and adding support for the Govee H6005 bulb (see Usage below).

I have tested and confirmed this to work with the H6001 and H6005 LED Light Bulbs, [and based on this](https://github.com/egold555/Govee-Reverse-Engineering/blob/master/Products/H6127.md) it should also work with the H6127 LED Strip Lights and maybe other Govee/Minger lights. I have only confirmed it to work on Mac, but it should also work on other platforms.

# Installation
Use pip to install:
```
pip install -U git+https://github.com/jonahclarsen/bluetooth_lights_controller
```

# Usage
```python
from bluetooth_lights_controller import BluetoothLED
import asyncio

lights = {  # Replace these with your LED's MAC address (see below for instructions to find)
    "bedroom": 'XX:XX:XX:XX:XX:XX',
    "lamp": 'XX:XX:XX:XX:XX:XX',
    "h6005": 'XX:XX:XX:XX:XX:XX', # For the Govee H6005 we need to include "h6005" in the name here
    }


async def main():
    for i in range(2): # For some reason, setting a color sometimes fails (maybe 1 in 50 times). You could then just re-run it manually, but I like doing every command twice so it basically never fails
        await set_color_of_all_lights_white(lights, -.45, 1)  # Day
        await set_color_of_all_lights(lights, 'orangered', 0.5)  # Evening
        await set_color_of_all_lights_white(lights, 0, 0)  # Night (off)

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
```

# Also included...
On the root of the repo, there are two additional Python scripts:
* ```govee_payload_generator.py``` generates the 20 bytes long payload that would be sent to the bulb via BLE. Useful for troubleshooting.
* ```search_btle.py``` returns a ```dict``` of MAC Addresses and Device Names of the devices of interest given a search phrase. Useful to integrate into programs where you do not know the MAC Address of the BLE devices you want to interact with (e.g. a room full of Govee bulbs...) To use this, simply call ```print(search_btle("minger"))``` or ```print(search_btle("600"))``` (my Govee H6005 showed up as 'ihoment_H6005_664B').

# Reverse Engineering of H6001 BLE Packets
[Have a look here for how the BLE packets that control the state of the LED bulb were reverse engineered.](https://github.com/egold555/Govee-Reverse-Engineering/blob/master/Products/H6127.md) [There is also some information on chvolkmann's original repo, which I used to figure out H6005 support.](https://github.com/chvolkmann/govee_btled)
