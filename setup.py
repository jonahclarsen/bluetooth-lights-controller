from setuptools import setup

setup(
    name='bluetooth_lights_controller',
    version='1.0',

    description='Govee Bluetooth RGB LED Controller',

    author='Jonah Larsen',
    author_email='email@email.com',

    packages=['bluetooth_lights_controller'],
    install_requires=[
        'bleak',
        'colour'
    ]
)