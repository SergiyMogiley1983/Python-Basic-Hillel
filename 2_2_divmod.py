x = int(input("Enter 5-digit number: "));
digit1 = divmod(x, 10);
print(digit1[0]);
digit2  = divmod(digit1[1], 100);
print(digit2[0]);
digit3 = divmod(digit2[1], 10);
print(digit3[0]);
print(digit3[1]);