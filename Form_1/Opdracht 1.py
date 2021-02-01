# pyramide
################################## opdracht 1 ##################################
def opdracht_1():
    i = int(input("hoe groot?"))
    for a in range(0, i):
        print('*' * a)
    for a in range(i, 0, -1):
        print('*' * a)
    a = 0
    while a != i:
        a += 1
        print('*' * a)
    while a != 0:
        a -= 1
        print('*' * a)

    while a != i:
        a += 1
        print(' ' * (i - a) + '*' * a)
    while a != 0:
        a -= 1
        print(' ' * (i - a) + '*' * a)



################################## opdracht 2 ##################################
def tekstcheck():
    string_1 = input("geef string 1:\n")
    string_2 = input("geef string 2:\n")
    shortest = 0
    if len(string_1) < len(string_2):
        shortest = len(string_1)
    else:
        shortest = len(string_2)
    verschil = 0
    for i in range(0, shortest):
        if string_1[i] == string_2[i]:
            verschil += 1
        else:
            print(f'het eerste verschil zit op index {verschil}')


################################## opdracht 3 ##################################

def count(x, lst):
    count = 0
    # lst = [0, 1, 5, 3, 54, 1, 47, 45, 16, 45, 88, 1, 2, 3, 4, 5]
    for i in range(0, len(lst)):
        if lst[i] == x:
            count += 1
    return (count)




def verschil_lst():
    lst_1 = [0, 1, 5, 3, 54, 1, 47, 45, 16, 45, 88, 1, 2, 3, 4, 5]
    biggest = 0
    for i in range(0, len(lst_1) - 1):
        tmp = 0
        if lst_1[i] > lst_1[i + 1]:
            tmp = lst_1[i] - lst_1[i + 1]
        elif lst_1[i + 1] > lst_1[i]:
            tmp = lst_1[i + 1] - lst_1[i]
        else:
            tmp = 0
        if tmp > biggest:
            biggest = tmp
    print(f'grootste verschil = {biggest}')


# verschil_lst()

def opdracht3c(lst):
    return True if count(1, lst) > count(0, lst) and count(0, lst) < 13 else False

#print(opdracht3c([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


################################## opdracht 4 ##################################

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
    return word == word[::-1]

################################## opdracht 5 ##################################
def my_sort(lst):
    """
    Sorteer gegeven lijst lst volgens het algoritme zoals beschreven in de pseudocode bij 1. hierboven.
    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.
    """
    sorted_list = lst.copy()
    waarde_index = 0

    while True:#for index in range(1,len(sorted_list)):
        if waarde_index+1 < len(lst):
            if sorted_list[waarde_index+1] < sorted_list[waarde_index]:
                sorted_list[waarde_index+1], sorted_list[waarde_index] = sorted_list[waarde_index], sorted_list[waarde_index+1]
                waarde_index = 0
            else:
                waarde_index +=1
        else:
            break

    return sorted_list
#print(my_sort([5,10,4,1,20]))

################################## opdracht 6 ##################################

def gemiddelde(lst):
    n = len(lst)
    total = 0
    for items in lst:
        total += items

    """ Retourneer het gemiddelde (float) van de lijst lst. """
    return total / n

def gem_2(lst):
    end_lst =[]
    for item in lst:
        n = len(item)
        total = 0
        for items in item:
            total += items
        """ Retourneer het gemiddelde (float) van de lijst lst. """
        end_lst.append(total / n)
    return end_lst

#print(gem_2([[1,2,3,4],[2,2,2]]))

################################## opdracht 7 ##################################
from random import randint
def random_game():
    i = randint(1,10)
    while int(input("what number did i get\n")) != i:
        print("try again")
    print("succes!")
random_game()
################################## opdracht 10 ##################################

def fibonaci(l, n0=0, n1=1):
    # lst.append(lst[len(lst) - 1] + lst[len(lst) - 2])
    return fibonaci(l - 1, n1, n0 + n1) if l != 0 else n0

# print(palindroom_2('racecar'))
