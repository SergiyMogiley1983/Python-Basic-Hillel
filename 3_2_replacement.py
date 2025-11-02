lst = [12, 3, 4, 10] #=> [10, 12, 3, 4]
#lst = [1] #=> [1]
#lst = [] #=> []
#lst = [12, 3, 4, 10, 8] #=> [8, 12, 3, 4, 10]

list_len = len(lst);
if list_len == 0:
    print(lst);
else:
    del_element = lst.pop(list_len-1);
    lst.insert(0, del_element);
    print(lst);