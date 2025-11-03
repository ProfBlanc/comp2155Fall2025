import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname="192.168.198.128",
    username="root",
    password="pnet",
    port=22
)