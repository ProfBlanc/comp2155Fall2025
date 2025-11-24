import telnetlib
import time


tn = telnetlib.Telnet("192.168.198.128", 30008)

# Wait until router is ready
tn.read_until(b"Press RETURN to get started", timeout=20)

# Press ENTER to get prompt
tn.write(b"\n")
time.sleep(1)

# Read initial output
output = tn.read_very_eager().decode()
print("Initial output:", output)

# Detect prompt from output
prompt = b">"

# Send command
tn.write(b"show ip int brief\n")
time.sleep(1)

# Read until prompt reappears
output = tn.read_until(prompt).decode()
print(output)

tn.close()
