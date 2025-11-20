def find_unique_value(some_list):
    res = some_list[0]
    count_of_1_elem = 0
    while count_of_1_elem != 1:
        first_elem = some_list[0]
        count_of_1_elem = some_list.count(first_elem)
        if count_of_1_elem == 1:
            res = first_elem
        else:
            some_list = [item for item in some_list if item != first_elem]
    return res
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([5]) == 5, 'Test4'
print("ОК")