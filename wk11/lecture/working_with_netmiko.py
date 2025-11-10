from netmiko_connect import connection


prompt = connection.find_prompt()
print(prompt)
result = connection.send_command("ls")
print(result)

commands = "mkdir d1,mkdir d2, mkdir d1/d3".split(",")

connection.send_config_set(commands)

result = connection.send_command("ls")
print(result)
