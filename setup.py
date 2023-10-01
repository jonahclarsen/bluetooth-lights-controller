from setuptools import setup

setup(
    name='bluetooth-lights-controller',
    version='1.0',

    description='Govee Bluetooth RGB LED Controller',

    author='Jonah Larsen',
    author_email='email@email.com',

    packages=['bluetooth-lights-controller'],
    install_requires=[
        'bleak',
        'colour'
    ]
)