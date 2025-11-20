import string
def is_palindrome(text):
    #прибираємо розділові знаки і пробіли в тексті, переводимо текст в нижній регістр
    new_text = "".join(char for char in text if (char not in string.punctuation and not char.isspace())).lower()
    return list(new_text) == list(new_text)[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")