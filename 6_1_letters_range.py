#"a-c" -> abc
#"a-a" -> a
#"s-H" -> stuvwxyzABCDEFGH
#"a-A" -> abcdefghijklmnopqrstuvwxyzA

import string
letters_range = input('Enter a range of letters: ')
start_index = string.ascii_letters.index(letters_range[0])
end_index = string.ascii_letters.index(letters_range[-1])
print(string.ascii_letters[start_index:end_index + 1])