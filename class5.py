"""
def calculation():
    a = 2
    b = 5
    x = a * b
    print(x)

calculation()


def plus(a,b):
    p = a + b
    print(p)

plus(10, 20)

def minus(a,b):
    m = a - b
    print(m)

minus(30,22)

def multiple(a,b):
    mm = a * b
    print(mm)

multiple(13,5)

def divided(a,b):
    d = a / b
    dd = int(d)
    print(dd)

divided(30,5)

def product(*args):
    sum = 0
    for result in args:
        sum += result

    return sum

Tuhin =  product(45,3443,343)
print(Tuhin)

shofiq = product(334,53,43)
print(shofiq)


# def product2(*args):
#     anything = 0
#     for result2 in args:
#         anything += result2

#     return anything

# me = product2(34,34,43)
# print(me) 


def product2(**kwargs):
    anything = 0
    for result2 in kwargs:
        anything += kwargs[result2]

    return anything

me = product2(x=34,y=34,z=43)
print(me)

"""

# productList = {
#     salt = 20,
#     potato = 34,
#     oil = 170,
#     rice = 78,
#     fish = 289,
#     banana = 15,
# }

productList = [56,7,45,765,345]
sum = 0
for Total in productList:
    sum += Total
print(sum)




def product():
    productList = [56,7,45,765,345]
    sum = 0
    for Total in productList:
        sum += Total
    print(sum)
# tomal = product(potato,oil)

# print(tomal)
product()
product()
product()
product()
product()
product()
product()




product3 = lambda a,b,c: a + b + c
you = product3(23,423,42)
print(you)