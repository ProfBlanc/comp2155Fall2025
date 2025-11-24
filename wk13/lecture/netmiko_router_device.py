import sys

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.198.128",
    "username": "",
    "password": "",
    "port": 30008,
    "secret": "cisco1"
}
connection = False
try:
    connection = ConnectHandler(**device)
    print("Successfully connected to device with host of",
          connection.host, "and device", connection.device_type)
    print("Prompt=", connection.find_prompt())
    connection.enable()
    print("Prompt=", connection.find_prompt())
    result = connection.send_command("show ip int brief")
    print(result)
except Exception as e:
    print(e, file=sys.stderr)
finally:
    if not isinstance(connection, bool):
        connection.disconnect()