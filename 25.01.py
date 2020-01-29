#1 задание

my_list = [14,1.2,'вася']
l = len(my_list)
while l > 0:
    l = l - 1
    print(my_list[l],type(my_list[l]))

# 2 задание

my_list = list(input('Ввведите ваш лист '))
print('Ваш лист', my_list)
l = (len(my_list)/2)
x = 0
y = 2
new_list = my_list[x:y:1]
new_list.reverse()
while y < l*2:
    x = x + 2
    y = y + 2
    new_list1 = my_list[x:y:1]
    new_list1.reverse()
    new_list.extend(new_list1)
print('Результат', new_list)

#3 задание
'''




#winter = [1,2,12]
#spring = [3,4,5]
#summer = [6,7,8]
#autumn = [9,10,11]

season = dict(Зима = 1, Весна = [3,4,5], Лето =[6,7,8], Осень = [9,10,11])
x = (input('Введите числовое значение месяца от 1 до 12 '))
    print(season.get(x))
    
'''

#4 задание
my_str = input('Введите строку из нескольких слов')
x = my_str.split()
l_str = len(x)
l = 0
while l < l_str:
    print(l+1, x[l][0:9])
    l = l + 1

# 5 задание
my_list = [7, 5, 3, 3, 2]
x = int(input('Введите число'))
if x in my_list:
    y = my_list.index(x)
    my_list.insert(y,x)
    print(my_list)
elif x > my_list[0]:
    my_list.insert(0, x)
    print(my_list)
elif x < my_list[-1]:
    my_list.append(x)
    print(my_list)

#6 задание

#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
'''
"x = int(input('Введите кол-во позиций '))
i = 0
while i < x:
    i = i+1
    name = input('Введите название товара под номером')
    price = input('Введите  цену товара под номером',)
    numbers = input('Введите кол-во товара под номером',)
    point = input('Введите единицы измерения товара под номером',)
    my_t = (i,name, price,numbers, point)
    print(my_t)
'''