from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
  "host": 'nxos2.lasthop.io',
  "username": 'pyclass',
  "password": getpass(),
  "device_type": 'cisco_nxos_ssh',
  "global_delay_factor": 2,
  }

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
  
start_time = datetime.now()
output = net_connect.send_command("show lldp neighbors detail")
end_time = datetime.now()

print("~" * 80)
print(output)
print("~" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()
  
start_time = datetime.now()
output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
end_time = datetime.now()

print("~" * 80)
print(output)
print("~" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()
