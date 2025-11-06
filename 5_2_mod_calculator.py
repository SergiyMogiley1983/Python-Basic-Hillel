while True:
    x = float(input('Enter the first number: '));
    y = float(input('Enter the second number: '));
    a = input('Enter operation: ');
    if a == '+':
        print(round(x+y, 3));
    elif a == '-':(
        print(round(x-y, 3)));
    elif a == '*':
        print(round(x*y, 3));
    elif a == '/':
        if y == 0:
            print('Division by zero!');
        else:
            print(round(x/y, 3));
    else: print('Invalid operation!');
    #перевірка бажання користувача продовжувати
    answer = input('Do you want to continue? (y/n): ');
    if answer != 'y': #будь-яка відповідь, крім y(yes), вважається відмовою
        break;
    else:
        continue;