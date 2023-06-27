#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

# password = getpass()

SW1 = {
    "device_type": "cisco_ios",
    "host": "10.0.0.32",
    "username": "admin",
    "password": "access123",
}

SW2 = {
    "device_type": "cisco_ios",
    "host": "10.0.0.30",
    "username": "admin",
    "password": "access123",
}

SW3 = {
    "device_type": "cisco_ios",
    "host": "10.0.0.29",
    "username": "admin",
    "password": "access123",
}

SW4 = {
    "device_type": "cisco_ios",
    "host": "10.0.0.31",
    "username": "admin",
    "password": "access123",
}
command = "show int trunk"
for device in (SW1, SW2, SW3, SW4):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    print(net_connect.send_command(command))
    net_connect.disconnect()



