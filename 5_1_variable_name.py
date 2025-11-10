#_ => True
#__ => False
#___ => False
#x => True
#get_value => True
#get value => False
#get!value => False
#some_super_puper_value => True
#Get_value => False
#get_Value => False
#getValue => False
#3m => False
#m3 => True
#assert => False
#assert_exception => True
#super_puper__value => True
#!et_value => False

import keyword
import string
txt = input("Enter a string: ")
#Послідовно перевіряємо кожне з обмежень задачі, присвоюючи відповідній змінній логічне значення
first_is_digit = False    #перший елемент - цифра
has_upper_letters = False #є великі літери
registered_word = False   #є зареєстрованим словом
has_spaces = False        #є пробіли
has_punctuation = False   #є знаки пунктуації, крім "_"
too_many_ = False         #повне ім'я змінної складається більш ніж з одного нижнього підкреслення
string_is_variable = True #вважаємо, що рядок може бути змінною (за замовчуванням)
#Чи починається рядок з цифри?
if txt[0].isdigit():
    first_is_digit = True
#Чи містить рядок великі літери?
if not txt == txt.lower():
    has_upper_letters = True
#Чи є рядок зареєстрованим словом?
for key_word in keyword.kwlist:
    if txt == key_word:
        registered_word = True
#Чи містить рядок пробіли?
for char in txt:
    if char.isspace():
        has_spaces = True
#Чи містить рядок знаки пунктуації, крім "_"?
no_punctuation_txt = "".join(char for char in txt if (char not in string.punctuation or char == '_'))
if not txt == no_punctuation_txt:
    has_punctuation = True
#Чи не забагато нижніх підкреслень?
if len(txt) > 1 and len(txt) == txt.count('_'):
    too_many_ = True
#Визначаємо, чи не виконалася хоча б одна з заборонених умов
if first_is_digit or has_upper_letters or registered_word or has_spaces or has_punctuation or too_many_:
    string_is_variable = False
print(string_is_variable)
