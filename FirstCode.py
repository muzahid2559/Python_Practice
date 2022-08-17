# Global Scope and Local Scope

def f():
    c = 10
    print(c)

f()


def function():
    global  a
    print(a+23)

function()


def pop(): # this code output is error
    print(x)
    x = 50

x =100
pop()