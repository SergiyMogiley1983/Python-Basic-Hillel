x = int(input("Enter 4-digit number: "));
digit1 = x//1000;
print(digit1);
digit2  = (x-1000*digit1)//100;
print(digit2);
digit3 = (x-1000*digit1-100*digit2)//10;
print(digit3);
digit4 = x-1000*digit1-100*digit2-10*digit3;
print(digit4);