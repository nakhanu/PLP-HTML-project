n1 = float (input('Enter first number '))
operator = input("Enter the operator (+,-,*,/:) ")
n2 = float (input('Enter second number '))
if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2
elif operator == '/':
    if n2 != 0:
        result = n1/n2
    else:
        result = "Error!"
else:
    result = "Invalid operator"
print (f"{n1} {operator} {n2} = {result}")



