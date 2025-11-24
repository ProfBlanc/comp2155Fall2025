import sys

from netmiko import ConnectHandler, FileTransfer, SCPConn

device = {
    "device_type": "linux",
    "host": "192.168.198.128",
    "username": "root",
    "password": "pnet",
    "port": 22,
    "secret": "pnet"
}
connection = False
try:
    connection = ConnectHandler(**device)
    print(f"Successfully connected to {connection.host} on device {connection.device_type}")

    # Create the file to upload to device
    source_file = "test1.txt"
    with open(source_file, "w") as file:
        file.write("Hello from our host machine!")

    destination_file = "d1/sent1.txt"
    """
    result = FileTransfer(
        connection,
        source_file=source_file,
        dest_file=destination_file,
        file_system="flash:",
    )
    result.transfer_file()
    """
    transfer = SCPConn(ssh_conn=connection)
    transfer.scp_put_file(source_file=source_file, dest_file=destination_file)
    transfer.close()
except Exception as e:
    print(e, file=sys.stderr)
finally:
    if not isinstance(connection, bool):
        connection.disconnect()
