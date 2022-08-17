# series - 1+2+3+4
sum = 0
for i in range(1,5):
    sum = sum +i
    print(i)
print("Sum =", sum)


# series - 1^2+2^2+3^2+4^2
sum = 0
for i in range(1,5):
    sum = sum +i*i
    print(i*i)
print("Sum =", sum)


# series - 1+3+5+7
odd = 0
for i in range(1,8,2):
    odd = odd +i
    print(i)
print("Sum =", odd)


# series - 2+4+6+8
even = 0
for i in range(0,9,2):
    even = even +i
    print(i)
print("Sum =", even)

# complex series - 1+(1+2)+(1+2+3)+(1+2+3+4)
sum = 0
for i in range(1,5):
    for j in range(1,i+1):
        sum = sum+j
print(sum)