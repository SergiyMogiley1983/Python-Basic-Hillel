def popular_words (text, words):
    res = {}                                                 #результат роботи - словник, поки порожній
    low_text_split = [elem.lower() for elem in text.split()] #переводимо всі слова тексту списком в нижній регістр
    for word in words:
        k = low_text_split.count(word)                       #рахуємо кількість входжень слова в список
        res[word] = k                                        #додаємо ключ-значення в словник
    return dict(sorted(res.items(), key = lambda x:x[1], reverse = True))
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
assert popular_words('''Roses are red Violets are blue Sugar is sweet And so are you''', ['is', 'are', 'fire']) == {'are': 3, 'is': 1, 'fire': 0}, 'Test2' #додатковий тест
print('OK')