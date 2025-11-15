def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"
    #return "Hi. My name is {0} and I'm {1} years old".format(name, age)
    #return "Hi. My name is " + name + " and I'm " + str(age) + " years old"
assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
#assert say_hi("Vasya", 101) == "Hi. My name is Vasya and I'm 101 years old", 'Test3'
print('ОК')
