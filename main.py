if __name__ == '__main__':


 a = 4
# b = 5
# a = b
# print(id(a))
# print(id(b))

# a = [1,2]
# print(id(a))
# a = [1,3]
# print(id(a))

# a = (1, 2, [6, 6],)
# print(id(a))
# a[2].append(6)
# print(a)
# print(id(a))
# a = (1,2, [1,5],)
# print(id(a))

#  mission complate
# numbers = (1, 3, 4, 2,[ 8, 5,],3,)
# print(id(numbers))
# array = numbers.count(3)
# print(array)
# print('count of 2:', array)

   # mission complate
# numbers = (1, 3, 4, 2,[ 8, 5,],8,)
# print(id(numbers))
# print(array)
# print(numbers.index(8)

# array = ['1', '2', '3', '4']
# array.pop(3)
# print('Updated List: ', array)
# print(array.index('3'))

     #пример
#  d = {}
#  d
# {}
#  d = {'dict': 1, 'dictionary': 2}
#  d
# {'dict': 1, 'dictionary': 2}


# d = {"1": 1}
# d["1"] = 1
# print(d)
#--------------------------------------------------------------------------------------------------------------


# Удаляет из словаря все элементы.
# d = {1: "one", 2: "two"}
#
# d.clear()
# print('d =', d)


# Просто копирует)
# array = {'Физика':67, 'Математика':87}
# nite = array.copy()
# print('array:', array)
# print('nite:', nite)



# keys = {'n', 'a', 'd', 'i', 'r' }
# vowels = dict.fromkeys(keys)
# print(vowels)


# добовляет скобки (я примерно так понял)
# array = {'Физика':67, 'Математика':87}
# print(array.items())


# показывает то что написал
# marks = {'Физика':67, 'Матиматика':69}
# print(marks.get('Maths'))



# я четсно без понятия что оно делает, убирает объект после двоеточия)
# array = {'I': 'Phill', 'love': 22, 'you': 3500.0}
# print(array.keys())
# empty_dict = {}
# print(empty_dict.keys())


# показывает то что ввел)
# marks = { 'Физика': 67, 'Геометрия': 72, 'Матиматика': 69 }
# element = marks.pop('Матиматика')
# print('Popped Marks:', element)



# биография)
# array = {'nadir': 'tynarov', 'age':16, 'salary': 20000}
# result = array.popitem()
# print('Return Value = ', result),print('person = ', array)
# array['профессия'] = 'прогроммист'
# result = array.popitem()
# print('Return Value = ', result)
# print('person = ', array)


#
# array = {'nadir': 'HAN', 'age': 22}
# age = array.setdefault('age')
# print('person = ',array)
# print('Age = ',age)



# # добовляет то что нужно)
# marks = {'Физика':67, 'Матиматика':87}
# internal_marks = {'Физкультура':100}
# marks.update(internal_marks)
# print(marks)



# бирает слова и остаовляет лишь цыфры)
# array = {'ФИзика':69, 'Математика':96}
# print(array.values())