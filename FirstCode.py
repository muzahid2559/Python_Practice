# To check a number is armstrong or not
digit = int(input("Enter the number"))
temp = digit
sum = 0

while digit !=0:
    digit_mod = digit % 10
    digit = digit // 10
    sum = sum + digit_mod**3
if sum == temp:
    print("The number is armstrong")
else:
    print("The number is not armstrong")