# use of infinite Loop and break statement
while True:
    name = input("Please Enter your Name :")
    if name == "Muzahid":
        break
    print(name)
print("Thank You")

# use of infinite Loop and continue statement
while True:
    name = input("Who are you :")
    if name == "Batman":
        continue
    print("Hello There "+name+" What is your password")
    password = input()
    if password == "icecream":
        break
print("Thank You")