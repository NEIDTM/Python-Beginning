import asyncio
import os


list = ['1. Your data', '2. None', '3. None', '4. None']

print("What you want?")
print(list)

choice = int(input("Choose the function, by typing the number: "))

async def your_data():
    name = input("Type your name: ")
    await asyncio.sleep(1)
    print(f"Got it, your name is {name}!")
    
    surname = input("Type your surname: ")
    await asyncio.sleep(1)
    print(f"Got it, your surname is: {surname}!")

    age = input("Type your age: ")
    await asyncio.sleep(1)
    print(f"Got it, your age is {age}!")

    folder_path = "C:Users\\Neid\\Desktop"
    file_name = "YourData.txt"
    file_path = os.path.join(folder_path, file_name)

    file = open(file_path, "w")
    file.write(f"{name}, {surname}, {age}")
    file.close
    await asyncio.sleep(3)
    print("Your data was created!")

if choice == 1:
    asyncio.run(your_data())
else:
    print("Sorry, we are still working on it!")