# 1 задание
def delenie ():
    x = int(input("Укажите первое число: "))
    y = int(input("Укажите второе число: "))
    if y == 0:
        print("На ноль делить нельзя")
    else :
        z = x / y
        return z
print(delenie())

# 2 задание

def func(name, surname, birth, city, email, telefon):
    x = print(name, surname, birth, city, email, telefon)
    return x
print(func('Александр', 'Якшевич', '18.11.1986', 'Ленинград', '7723588@gmail.com', '89215728044'))



# 3 задание
def my_func(x, y, z):
    a = max(1, 2, 3)

    print(a)
print(my_func(1, 2, 3))