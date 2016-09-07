from distutils.core import setup

setup(
    name='wificontrol',
    version='0.0.1.dev1',
    author='Ivan Sapozhkov',
    author_email='i.sapozhkov.93@gmail.com',
    py_modules=['wificontrol'],
    #packages=['wificontrol'],
    url='https://github.com/emlid/reach-wifi-configurator.git',
    #license='LICENSE.txt',
    description='Module for contol WiFi connections with host(AP) and client(WPA) modes.',
    long_description=open('README.md').read(),
)