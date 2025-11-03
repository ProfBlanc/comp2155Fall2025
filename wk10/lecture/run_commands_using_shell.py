from paramiko_connect import client
import time

shell = client.invoke_shell()

shell.send("ls\n")
time.sleep(2)
response = shell.recv(1000)
output = response.decode()
print(output)
