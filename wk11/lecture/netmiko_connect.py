from netmiko import ConnectHandler
# python -m pip install netmiko

connection = ConnectHandler(
    device_type="linux",
    username="root",
    password="pnet",
    host="192.168.198.128"
)