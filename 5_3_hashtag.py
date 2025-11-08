#'Python Community' -> #PythonCommunity
#'i like python community!' -> #ILikePythonCommunity
#'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string
txt = input("Enter a string: ")
txt = "".join(char for char in txt if char not in string.punctuation) #чистимо текст від спецсимволів (пробіли поки залишаються)
txt_words = txt.split() #розбиваємо текст на окремі слова, таким чином, позбуваючись пробілів
new_txt = '#' #результат завжди починається зі знака хештегу
for txt_word in txt_words:
    new_txt = new_txt + txt_word.capitalize()
print(new_txt[:140]) #обрізаємо текст до 140 символів