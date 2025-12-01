from netmiko import ConnectHandler
from robot.api.deco import keyword

@keyword
def connect_and_run_command(host, username, password, secret, port, command):

      
    device = {
        "device_type": "cisco_ios_telnet",
        "host": host,
        "username": username,
        "password": password,
        "secret": secret,
        "port": port,
    }
    
    conn = ConnectHandler(**device)
    conn.enable()
    output = conn.send_command(command)
    conn.disconnect()
    return output
