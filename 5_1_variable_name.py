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
#super_puper__value => False

import keyword
import string
txt = input("Enter a string: ")
#Послідовно перевіряємо кожне з обмежень задачі, присвоюючи відповідній змінній логічне значення
firstIsDigit = False    #перший елемент - цифра
hasUpperLetters = False #є великі літери
registeredWord = False  #є зареєстрованим словом
hasSpaces = False       #є пробіли
hasPunctuation = False  #є знаки пунктуації, крім "_"
hasDouble_ = False      #є "__"
stringIsVariable = True #вважаємо, що рядок може бути змінною (за замовчуванням)
#Чи починається рядок з цифри?
if txt[0].isdigit():
    firstIsDigit = True
#Чи містить рядок великі літери?
if not txt == txt.lower():
    hasUpperLetters = True
#Чи є рядок зареєстрованим словом?
for key_word in keyword.kwlist:
    if txt == key_word:
        registeredWord = True
#Чи містить рядок пробіли?
for char in txt:
    if char.isspace():
        hasSpaces = True
#Чи містить рядок знаки пунктуації, крім "_"?
if txt.count('_') == 0:
    for char in txt:
        if char in string.punctuation:
            hasPunctuation = True
if not hasPunctuation and txt.count('_') > 1: #один знак "_" завжди допускається
    if txt.count('__') > 0:
                hasDouble_ = True
#Визначаємо, чи не виконалася хоча б одна з заборонених умов
if firstIsDigit or hasUpperLetters or registeredWord or hasSpaces or hasPunctuation or hasDouble_:
    stringIsVariable = False
print(stringIsVariable)