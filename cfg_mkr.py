from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {
  "host": 'nxos1.lasthop.io',
  "username": 'pyclass',
  "password": password,
  "device_type": 'cisco_nxos_ssh',
# "fast_cli": True,
}

device2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_nxos_ssh',
  # "fast_cli": True,
}

net_connect = ConnectHandler(**device1)

output = net_connect.send_config_from_file(config_file='vlan_adds.txt')
print()
print("#" * 80)
print("CFG Change: ")
print(output)
print("#" * 80)
print()

save_out = net_connect.save_config()
print(save_out)

net_connect.disconnect()

net_connect = ConnectHandler(**device2)

output = net_connect.send_config_from_file(config_file='vlan_adds.txt')
print()
print("#" * 80)
print("CFG Change: ")
print(output)
print("#" * 80)
print()

save_out = net_connect.save_config()
print(save_out)

net_connect.disconnect()
