# Conditional Statement
# Find the largest number out of three numbers

A = input('Enter First Number : ')
B = input('Enter Second Number : ')
C = input('Enter Third Number : ')

if A > B:
    if A > C:
        print(f"{A} is Greater than {B} and {C}")
    else:
        print(f"{C} is Greater than {A} and {B}")
if A < B:
    if C < B:
        print(f"{B} is Greater than {A} and {C}")
    else:
        print(f"{C} is Greater than {A} and {B}")
