"""
2 numbers, a,b
4 operators
c for storing result
while loop to continue
break if enteres = and show c
store c in a and ask for b and perform operations
4 methods for operations

"""


def add(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2

class calculation:
    num1 = int(input("enter number 1: "))
    result = 0
    while True:
        oper = input("enter the operator [+,-,*,/]: ")
        num2 = int(input("enter number 2: "))
        if oper == '+':
            result = add(num1, num2)
            num1 = result
            print(f'result: {result}')
        elif oper == '-':
            result = minus(num1, num2)
            num1 = result
            print(f'result: {result}')
        elif oper == '*':
            result = mul(num1, num2)
            num1 = result
            print(f'result: {result}')
        elif oper == '/':
            result = div(num1, num2)
            num1 = result
            print(f'result: {result}')
        elif oper == '=':
            print(f'result: {result}')
            break
        else:
            print("invalid choice, please enter [+,-,*,/]")
