import sys

from napalm import get_network_driver

driver = get_network_driver("ios")

connection = driver(
    hostname="192.168.198.128",
    username="",
    password="",
    timeout=5,
    optional_args={
        "port": 30008,
        "transport": "telnet",
        "secret": "cisco1"
    }
)

try:
    connection.open()

    interfaces = connection.get_interfaces()
    interfaces_ip = connection.get_interfaces_ip()

    print(interfaces)
    print(interfaces_ip)


except Exception as e:
    print(e, file=sys.stderr)
finally:
    connection.close()