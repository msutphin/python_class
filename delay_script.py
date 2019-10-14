from netmiko import ConnectHandler
from getpass import getpass

device = {
  "host": 'nxos2.lasthop.io',
  "username": 'pyclass',
  "password": getpass(),
  "device_type": 'cisco_nxos_ssh',
  "global_delay_factor": 2,
  }
  
  net_connect = ConnectHandler(**device)
  print(net_connect.find_prompt())
  
  output = net_connect.send_command("show lldp neighbors detail")
  print(output)

  output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
  print(output)
