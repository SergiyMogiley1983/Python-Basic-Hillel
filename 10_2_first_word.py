def first_word(text):
    mapping_dict = {",": " ", ".": " "} #крапки й коми замінимо на пробіли
    translation_table = str.maketrans(mapping_dict)
    translated_text = text.translate(translation_table)
    return translated_text.split()[0]
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')