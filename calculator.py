first_number = int(input("Type your first number: "))

print(f"""
Your first number is {first_number}""")

action = int(input("""
Choose an action:
1. Sum
2. Difference
3. Division
4. Multiplication

"""))

if action == 1:
	print(f"""
You selected function sum""")

if action == 2:
	print(f"""
You selected function difference""")

if action == 3:
	print(f"""
You selected function division""")

if action == 4:
	print(f"""
You selected function multiplication""")

second_number = int(input("""
Type your second number: """))

print(f"""
Your second number is {second_number}""")

def sum():
	equals = 0
	equals = first_number + second_number
	return equals

def diff():
	equals = 0
	equals = first_number - second_number
	return equals

def div():
	equals = 0
	equals = first_number / second_number
	return equals

def mult():
	equals = 0
	equals = first_number * second_number
	return equals

if action == 1:
    print(f"""
{first_number} + {second_number} = {sum()}
""")

if action == 2:
    print(f"""
{first_number} - {second_number} = {diff()}
""")

if action == 3:
    print(f"""
{first_number} / {second_number} = {div()}
""")
    
if action == 4:
    print(f"""
{first_number} * {second_number} = {mult()}
""")