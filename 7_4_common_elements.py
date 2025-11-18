def common_elements():
    num_list_3 = [i for i in range(0, 100) if i % 3 == 0]
    num_list_5 = [j for j in range(0, 100) if j % 5 == 0]
    return set(num_list_3).intersection(set(num_list_5))
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}