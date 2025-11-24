from netmiko import ConnectHandler, FileTransfer

device = {
    "device_type": 'linux',
    "host": '192.168.198.128',
    "username": 'root',
    "password": 'pnet',
    "port": '22',
    }

connection = ConnectHandler(**device)
res1 = connection.send_command("telnet localhost 30008", expect_string="R4", read_timeout=30)
res1 = connection.send_command("\n")

print(res1)
#res2 = connection.send_command("enable", expect_string="Password:")
#res3 = connection.send_command("cisco1", cmd_verify=False)
#res2 = connection.find_prompt()
#print(res1, res2, sep='\n')