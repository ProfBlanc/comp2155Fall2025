from paramiko_connect import client

stdin, stdout, stderr = client.exec_command("ls")
print(stdout.read().decode())