import asyncio

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

async def sleep():
	await asyncio.sleep(5)
	print("Goodbye!")

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


async def action_one():
	result = (f"""
{first_number} + {second_number} = {sum()}""")
	print(result)
	await asyncio.sleep(2)
	file = open("history.txt", 'a')
	file.write(f"""{result}""")
	file.close()


async def action_two():
	result = (f"""
{first_number} - {second_number} = {diff()}""")
	print(result)
	await asyncio.sleep(2)
	file = open("history.txt", 'a')
	file.write(f"""{result}""")
	file.close()


async def action_three():
	result = (f"""
{first_number} / {second_number} = {div()}""")
	print(result)
	await asyncio.sleep(2)
	file = open("history.txt", 'a')
	file.write(f"""{result}""")
	file.close()


async def action_four():
	result = (f"""
{first_number} * {second_number} = {mult()}""")
	print(result)
	await asyncio.sleep(2)
	file = open("history.txt", 'a')
	file.write(f"""{result}""")
	file.close()


if action == 1:
	asyncio.run(action_one())

if action == 2:
	asyncio.run(action_two())

if action == 3:
	asyncio.run(action_three())

if action == 4:
	asyncio.run(action_four())
