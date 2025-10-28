x = int(input("Enter 5-digit number: "));
digit5 = x//10000;
digit4 = (x-10000*digit5)//1000;
digit3 = (x-10000*digit5-1000*digit4)//100;
digit2 = (x-10000*digit5-1000*digit4-100*digit3)//10;
digit1 = x-10000*digit5-1000*digit4-100*digit3-digit2*10;
print(digit1*10000+digit2*1000+digit3*100+digit4*10+digit5);
