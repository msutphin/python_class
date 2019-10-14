from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

start_time = datetime.now()

device = {
  "host": 'cisco3.lasthop.io',
  "username": 'pyclass',
  "password": password,
  "device_type": 'cisco_ios_ssh',
  "fast_cli": True,  
}

net_connect = ConnectHandler(**device)

cfg = [
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
]

output = net_connect.send_config_set(cfg)
print(output)

output = net_connect.send_command('ping google.com')
print(output)

net_connect.disconnect()

end_time = datetime.now()

print("Total Execution Time: {}\n".format(end_time - start_time))
