from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {    
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_ios_ssh',
}
net_connect = ConnectHandler(**device1)
output = net_connect.send_command("show version")

with open("show_version.txt", "w") as f:
    f.write(output)

net_connect.disconnect()
