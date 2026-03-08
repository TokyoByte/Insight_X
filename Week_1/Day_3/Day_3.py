def sum(a, b):
    return a+b

print(sum(3,8))

def print_Guest_name():
    print("default name = \"Guest\"")

print_Guest_name()

x = lambda a : a*a

print(x(8))

with open("new_file.text", "w") as file :
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")
    file.write("This is line 4\n")
    file.write("This is line 5\n")

print("File written")

with open("new_file.text", "r") as file :

    content = file.read()

    print(content)