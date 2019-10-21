import yaml
from pprint import pprint

device1 = {'device_name': 'cisco3', 'host': 'cisco3.lasthop.io'}
device2 = {'device_name': 'cisco4', 'host': 'cisco4.lasthop.io'}
device3 = {'device_name': 'nxos1', 'host': 'nxos1.lasthop.io'}
device4 = {'device_name': 'nxos2', 'host': 'nxos2.lasthop.io'}

all_devices = [device1, device2, device3, device4]

for device in all_devices:
    device['username'] = 'root'
    device['password'] = 'password1234'

pprint(all_devices)

with open('devices.yml', 'w') as txt:
    yaml.dump(all_devices, txt, default_flow_style=False)
