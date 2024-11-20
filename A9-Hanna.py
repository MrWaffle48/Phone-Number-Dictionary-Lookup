with open('phonelist.txt', 'r') as file:
    contents = file.read()

phoneList = [line.strip().split(',') for line in contents.split('\n') if line]

phoneDict = {name.lower(): phone for name, phone in phoneList}

print(phoneList)
print(phoneDict)

while True:
    name = input("Enter name: ")

    if not name:
        print("GoodBye.")
        break

    if name.lower() in phoneDict:
        print("Phone Number", phoneDict[name.lower()])
    else:
        print("Name not in phone listing.")
