import time

from govee_btled_windows import BluetoothLED

# Replace this with your LED's MAC address
led = BluetoothLED('XX:XX:XX:XX:XX:XX')

print('Switching on LED')
led.set_state(True)
time.sleep(.5)

print('Changing colors in RGB')
for color in ['red', 'green', 'blue', 'purple', 'yellow', 'cyan', 'orange', 'white']:
    print(f'[*] {color}')
    led.set_color(color)
    time.sleep(.5)

print('Changing brightness')
for i in range(5+1):
    val = i/5
    print(f'[*] {int(val*100):03d}%')
    led.set_brightness(val)
    time.sleep(.5)

print('Changing colors in white-mode')
for i in range(-20, 20+1):
    val = i/20
    print(f'[*] {abs(int(val*100)):03d}% {"warm" if val <= 0 else "cold"} white')
    led.set_color_white(val)
    time.sleep(.2)

print('Switching off LED')
led.set_state(False)