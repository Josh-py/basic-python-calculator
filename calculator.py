num1 = float(input('enter your first number: '))
operator = input('enter operator (+, -, *, /): ')
num2 = float(input('enter your second number: '))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print('invalid operator')
