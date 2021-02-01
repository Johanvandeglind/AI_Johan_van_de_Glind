#pyramide

def opdracht_1():
    i = int(input("hoe groot?"))
    for a in range(0,i):
        print('*' * a)
    for a in range(i,0,-1):
        print('*' * a)
    a= 0
    while a != i:
        a+=1
        print('*'*a)
    while a != 0:
        a-=1
        print('*'*a)

    while a != i:
        a+=1
        print(' '*(i-a) + '*'*a)
    while a != 0:
        a-=1
        print(' '*(i-a) + '*'*a)

#opdracht_1()
#

def tekstcheck():
    string_1= input("geef string 1:\n")
    string_2= input("geef string 2:\n")
    shortest = 0
    if len(string_1)<len(string_2):
        shortest = len(string_1)
    else:
        shortest = len(string_2)
    verschil = 0
    for i in range(0,shortest):
        if string_1[i] == string_2[i]:
           verschil +=1
        else:
            print(f'het eerste verschil zit op index {verschil}')

#tekstcheck()

def count(x):
    count = 0
    lst = [0,1,5,3,54,1,47,45,16,45,88,1,2,3,4,5]
    for i in range(0,len(lst)):
        if lst[i] == x:
            count +=1
    print(f'x kwam {count} keer voor in ')

#count(1)

def verschil_lst():
    lst_1 = [0,1,5,3,54,1,47,45,16,45,88,1,2,3,4,5]
    biggest = 0
    for i in range(0,len(lst_1)-1):
        tmp=0
        if lst_1[i]>lst_1[i+1]:
            tmp = lst_1[i] - lst_1[i+1]
        elif lst_1[i+1] > lst_1[i]:
            tmp = lst_1[i+1] - lst_1[i]
        else:
            tmp = 0
        if tmp > biggest:
            biggest = tmp
    print(f'grootste verschil = {biggest}')
# verschil_lst()




def palindroom(word):
    if len(word) == 0:
        return False
    elif len(word) == 1:
        return True
    else:
        if word[0] == word[-1]:
            return palindroom(word[1:-1])
        else:
            return False

def palindroom_2(word):
    return word==word[::-1]
print(palindroom_2('racecar'))