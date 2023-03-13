
import os
from netmiko import ConnectHandler
from getpass import getpass


USERNAME = input("Please enter your ssh username: ")
PASS = getpass("Please enter your ssh password: ")

device = {
    
    'ip': '192.168.60.129',
    'username' : USERNAME,
    'password' : PASS,
    'device_type' : 'cisco_ios'

}

c = ConnectHandler(**device)

output = c.send_command('show run')
print(output)




