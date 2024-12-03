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




