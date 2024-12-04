#################################
st = 'sdfs w 345 3dfg 34 '
def function(st):
    a=[]
    lenght = len(st)
    for i in range(lenght):
        if st[i].isdigit():
            a.append(int(st[i]))
    print(a)
def function2(st):
    a = []
    current = ''

    for char in st:
        if char.isdigit():
            current += char
        elif current:
            a.append(current)
            current = ''

    if current:
        a.append(current)

    print(a)



function(st)
function2(st)
#####################################
greeting = 'Hello, world'
lenghtInGreeting = len(greeting)
charGreeting=[]
for i in range(lenghtInGreeting):
    charGreeting.append(greeting[i].upper())
print(charGreeting)

n=1
quadro=[i*i for i in range(50)]
print(quadro)

###########################################
list = [10,10,10,10,10,6]





def function3(st):
    print(st)

def function4(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>a and c>b:
        return c

def function5(*numbers):
    smallest = min(numbers)
    largest = max(numbers)

    print("Найбільше число:", largest)
    return smallest

def function6(list):
    return min(list)

def function7(list):
    length = len(list)
    a=0
    for i in range(length):
        a+=list[i]
    print(a)
###################################################
lastList = [22, 3,5,2,8,2,-23, 8,23,5]
def min_from_list(lastList):
    return min(lastList)
def dublicate(lastList):
    print(set(lastList))





while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на "X"')
    print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('5) вывести табличку множення за допомогою цикла while')
    print('9) вихід')

    choice = input('Зробіть свій вибір: ')
    if choice == '1':
        min(lastList)
    if choice == '2':
        dublicate(lastList)
    if choice == '9':
        break







