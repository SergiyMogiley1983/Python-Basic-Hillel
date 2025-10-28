x = float(input('Enter the first number: '));
y = float(input('Enter the second number: '));
a = input('Enter operation: ');
if a == '+':
    print(round(x+y, 3));
elif a == '-':
    print(round(x-y, 3));
elif a == '*':
    print(round(x*y, 3));
elif a == '/':
    if y == 0:
        print('Division by zero!');
    else:
         print(round(x/y, 3));
else: print('Invalid operation!');