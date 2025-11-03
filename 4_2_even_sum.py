lst = [0, 1, 7, 2, 4, 8] #=> (0 + 7 + 4) * 8 = 88
#lst = [1, 3, 5] #=> 30
#lst = [6] #=> 36
#lst = [] #=> 0

sum_elem = 0; #присвоюємо сумі елементів початкове значення 0
#перевіряємо чи не пустий список
if len(lst) == 0:
    print(sum_elem); #виводимо результат
else:
    last_element = lst[-1]; #отримуємо останній елемент списку
    #перебираємо парні елементи списку і сумуємо їх
    for index, item in enumerate(lst):
        if index % 2 == 0:
            sum_elem += item;
    print(sum_elem*last_element); #виводимо результат