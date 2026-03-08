name  = "Shivansh"
age = 20
height = "170cm"

print(name, type(name))
print(age, type(age))
print(height, type(height))

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

sum = a+b

print(f"sum : {sum}")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
