# Methods of Dictionaries
identity = {'Name':'Muzahid','Age':'22','Job':'Student'}


# printing value
print(identity.values())

# printing keys
for i in identity.keys():
    print(i)

# printing value and keys
for i in identity.items():
    print(i)

# A handy trick
for k,v in identity.items():
    print('Key:'+ k +' value:'+v)

# use of 'in' keyword
print('Name' in identity)
print('pop' in identity)

# the get() method
print(str(identity.get('Name','DEFS')))
print(str(identity.get('pop','DEFS')))

# setdefault() Method

print(identity.setdefault('Name','DEFS'))
print(identity.setdefault('Height','12fit'))

print(identity)