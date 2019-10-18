import time
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

print("\nCurrent Prompt: ")
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

print("\nEnable Prompt: ")
net_connect.config_mode()
print(net_connect.find_prompt())

print("\nCurrent Prompt: ")
net_connect.exit_config_mode()
print(net_connect.find_prompt())

print("\nChannel Output: ")
net_connect.write_channel("disable\n")
time.sleep(2)
output = net_connect.read_channel()
print (output)

print("\nEnable Prompt:")
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()
print()
