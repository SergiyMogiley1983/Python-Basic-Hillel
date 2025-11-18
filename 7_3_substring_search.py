def second_index(text, some_str):
  index_1 = text.find(some_str)                    #шукаємо індекс першого входження підрядка
  if index_1 != -1:                                #якщо перше входження існує, тоді
      index_2 = text.find(some_str, index_1 + 1)   #шукаємо індекс другого входження підрядка
      if index_2 == -1:
          index_2 = None
  return index_2
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')