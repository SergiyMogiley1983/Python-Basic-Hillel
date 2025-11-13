#0 -> 0 днів, 00:00:00
#224930 -> 2 дні, 14:28:50
#397730 -> 4 дні, 14:28:50
#466289 -> 5 днів, 09:31:29
#950400 -> 11 днів, 00:00:00
#1209600 -> 14 днів, 00:00:00
#1900800 - > 22 дні, 00:00:00
#8639999 -> 99 днів, 23:59:59
#22493 -> 0 днів, 06:14:53
#7948799 -> 91 день, 23:59:59

number = int(input('Enter a number: '))
if not(0 <= number < 8640000):
    print('Wrong number!')
else:
    #розбиваємо число на дні-години-хвилини-секунди
    days_and_seconds = divmod(number, 86400)
    days = days_and_seconds[0]
    hours_and_seconds = divmod(days_and_seconds[1], 3600)
    hours = hours_and_seconds[0]
    minutes_and_seconds = divmod(hours_and_seconds[1], 60)
    minutes = minutes_and_seconds[0]
    seconds = minutes_and_seconds[1]
    #день, дні чи днів?
    days_word = 'днів,'                   #значення по замовчуванню
    if not(days % 100 in range(11, 20)):  #числа з 11 до 19 в кінці - все одно днів
        last_digit = days % 10
        if last_digit == 1:               #закінчуються на 1 - день
            days_word = 'день,'
        elif last_digit in range(2, 5):   #закінчуються на 2, 3, 4 - дні
            days_word = 'дні,'
    #виводимо результат в потрібному форматі
    time = str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2)
    print(days, days_word, time)