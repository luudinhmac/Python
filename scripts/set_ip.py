import subprocess
import socket
import platform

system = platform.system()
print(system)


def windows(ip, netmask, gw, card_name='Wi-Fi'):
    subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'address',
                             'name="'+card_name+'"', 'static', ip, netmask, gw])

def linux(ip, netmask, gw, card_name='ens33'):
    subprocess.run(['ifconfig', 'eth0', ip,
                   'netmask', netmask])


def set_ip(ip, netmask, gw, card_name='Wi-Fi'):
    if system == 'Linux':
        linux(ip, netmask, gw, card_name)
    elif system == 'Darwin':
        pass
    elif system == 'Windows':
        windows(ip, netmask, gw, card_name)


def test():
    try:
        sock = socket.create_connection(('www.google.com', 80))
        print("Connection established")
    except socket.error:
        print("Network error")


ip = '192.168.1.11'
netmask = '255.255.255.0'
gw = '192.168.1.1'
card_name = 'Wi-Fi'
print('name="'+card_name+'"')
set_ip(ip, netmask, gw)
test()
