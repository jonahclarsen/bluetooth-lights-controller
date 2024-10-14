import asyncio
from .bluetooth_led import BluetoothLED

timeout = 5.0  # Seems to work well

async def set_state_of_light(mac_address, state, is_h6005 = False):
    led = BluetoothLED(mac_address, timeout=timeout)
    boolt = await led.init_and_connect()
    if boolt is False:
        return
    await led.set_state(state)
    await led.disconnect()

async def set_color_of_light(mac_address, color, brightness, is_h6005 = False):
    led = BluetoothLED(mac_address, timeout=timeout)
    boolt = await led.init_and_connect()
    if boolt is False:
        return
    # await led.set_state(True)  # If your lights are ever turned off (i.e. via the app), uncomment this

    await led.set_color(color, is_h6005)
    await led.set_brightness(brightness)
    await asyncio.sleep(.05)
    await led.disconnect()


async def set_color_of_light_white(mac_address, color, brightness, is_h6005 = False):
    led = BluetoothLED(mac_address, timeout=timeout)
    boolt = await led.init_and_connect()
    if boolt is False:
        print("Failed to connect!")
        return
    # await led.set_state(True)  # If your lights are ever turned off (i.e. via the app), uncomment this

    await led.set_color_white(color, is_h6005)
    await led.set_brightness(brightness)
    await asyncio.sleep(.05)  # I found 0.009 worked and 0.001 didn't (but then later .001 worked...?; note I was
    # using 0.01 until MacOS 14 when it no longer worked, I had to switch to .05 like in the other func)
    await led.disconnect()


async def set_color_of_all_lights(lights, color, brightness):
    i = 0
    tasks = []
    for light_name, mac_address in lights.items():
        try:
            is_h6005 = False
            if "h6005" in light_name or "H6005" in light_name:
                is_h6005 = True

            tasks += [asyncio.create_task(set_color_of_light(mac_address, color, brightness, is_h6005))]
            i += 1
        except Exception as e:
            print("Exception in lights_controller:", e)

    for task in tasks:
        await task


async def set_state_of_all_lights(lights, state):
    i = 0
    tasks = []
    for light_name, mac_address in lights.items():
        try:
            is_h6005 = False
            if "h6005" in light_name or "H6005" in light_name:
                is_h6005 = True

            tasks += [asyncio.create_task(set_state_of_light(mac_address, state, is_h6005))]
            i += 1
        except Exception as e:
            print("Exception in lights_controller:", e)

    for task in tasks:
        await task


async def set_color_of_all_lights_white(lights, color, brightness):
    i = 0
    tasks = []
    for light_name, mac_address in lights.items():
        try:
            is_h6005 = False
            if "h6005" in light_name or "H6005" in light_name:
                is_h6005 = True

            tasks += [asyncio.create_task(set_color_of_light_white(mac_address, color, brightness, is_h6005))]
            i += 1
        except Exception as e:
            print("Exception!", e)

    for task in tasks:
        await task


def search_btle(device_of_interest=None):
    import asyncio
    from bleak import BleakScanner

    found_devices = []
    # device_of_interest = "minger"

    async def main():
        devices = await BleakScanner.discover()
        for d in devices:
            split_BLEDevice = (str(d).split(": "))
            if device_of_interest is None:
                found_devices.append({"address": split_BLEDevice[0], "name": split_BLEDevice[1]})
            elif device_of_interest in split_BLEDevice[1].lower():
                found_devices.append({"address": split_BLEDevice[0], "name":split_BLEDevice[1]})


    asyncio.run(main())
    return found_devices