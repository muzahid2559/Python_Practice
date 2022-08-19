# Open a file
f = open("a.txt","w")


# getting some info

print("name =",f.name)
print("is it closed? ",f.closed)
print("mode",f.mode)
f.write("Python is my favorite language.")

# appending to a file

f = open("a.txt","a")
f.write("I also love JavaScript.")
f.close()

# r+ functionaly
f = open("a.txt","r+")
info = f.read()
print(info)