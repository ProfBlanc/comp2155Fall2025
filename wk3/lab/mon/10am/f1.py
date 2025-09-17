file_name = "my.txt"

try:
    with open(file_name, "r") as fo:
        fo.write("Hello World")

except FileExistsError as e:
    print(e, "error 1")
except FileNotFoundError as e:
    print(e, "error 2")
except IOError as e:
    print(e, "error 3")