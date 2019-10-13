from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {    
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_nxos_ssh',
}

device2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_nxos_ssh',
}

for x in (device1, device2):
    net_connect = ConnectHandler(**x)
    print(net_connect.find_prompt())
    net_connect.disconnect()
