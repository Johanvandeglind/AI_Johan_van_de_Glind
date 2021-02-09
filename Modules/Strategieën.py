import itertools
import random
from Feedback import givefeedback

feedback = dict(round_0=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0]),
                round_1=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0]),
                round_2=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0]),
                round_3=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0]),
                round_4=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0]),
                round_5=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0]),
                round_6=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0]),
                round_7=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0]),
                round_8=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0]),
                round_9=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0]),
                black=0,
                white=0,
                red=0,
                yellow=0,
                blue=0,
                green=0)


def simple_strat(round: int, feedback: dict):
    """
    @param round:
    @param feedback:
    @return:
    """

    print(feedback["black"],feedback["white"],feedback["red"],feedback["yellow"],feedback["blue"],feedback["green"])
    code = []
    combi_lst = []
    if round == 0:
        code = [0, 0, 0, 0]
        return code
    elif len(combi_lst) > 0:
        lst = possible_combinations(combi_lst,feedback)
        lst = remove_doubles_code_lst(lst, combi_lst,feedback)
        print(lst)
    elif round == 1:
        print(feedback["round_0"]["black_pins"])
        feedback["black"] = feedback["round_0"]["black_pins"]
        return [1, 1, 1, 1]
    elif round == 2:
        print(feedback["round_1"]["black_pins"])
        feedback["white"] = feedback["round_1"]["black_pins"]

        if feedback["black"] + feedback["white"] == 4:
            combi_lst = check_right_colors(feedback)
            return [2, 2, 2, 2]
        else:
            return [2, 2, 2, 2]
    elif round == 3 and len(combi_lst) == 0:
        print(feedback["round_2"]["black_pins"])
        feedback["red"] = feedback["round_2"]["black_pins"]

        if feedback["black"] + feedback["white"]+ feedback["red"] == 4:
            combi_lst = check_right_colors(feedback)
            return [3, 3, 3, 3]
        else:
            return [3, 3, 3, 3]
    elif round == 4and len(combi_lst) == 0:
        print(feedback["round_3"]["black_pins"])
        feedback["yellow"] = feedback["round_3"]["black_pins"]

        if feedback["black"] + feedback["white"] + feedback["red"]+feedback["yellow"]==4:
            combi_lst = check_right_colors(feedback)
            print(combi_lst)
            return [4, 4, 4, 4]
        else:
            return[4,4,4,4]
    elif round == 5and len(combi_lst) == 0:
        feedback["blue"] = feedback["round_4"]["black_pins"]

        if feedback["black"] + feedback["white"] + feedback["red"] + feedback["yellow"] == 4:
            combi_lst = check_right_colors(feedback)
            return [5, 5, 5, 5]
        else:
            return [5, 5, 5, 5]
    elif round == 6 and len(combi_lst) == 0:
        feedback["green"] = feedback["round_5"]["black_pins"]
        combi_lst = check_right_colors(feedback)
        return [6, 6, 6, 6]
    elif round == 7 and len(combi_lst) == 0:
        feedback["green"] = feedback["round_5"]["black_pins"]
        combi_lst = check_right_colors(feedback)
        lst = possible_combinations(combi_lst)
        lst = remove_doubles_code_lst(lst,combi_lst,feedback)
        print(lst)


    return code


def check_right_colors(feedback:dict):
    combi_lst =[]
    if feedback["black"] > 0:
        combi_lst.append(0)
    if feedback["white"] > 0:
        combi_lst.append(1)
    if feedback["red"] > 0:
        combi_lst.append(2)
    if feedback["yellow"] > 0:
        combi_lst.append(3)
    if feedback["blue"] > 0:
        combi_lst.append(4)
    if feedback["green"] > 0:
        combi_lst.append(5)
    return combi_lst

def remove_doubles_code_lst(lst:list,combi_lst:list,feedback:dict):
    if len(combi_lst) == 4:
        remove_index =[]
        for item in lst:
            if combi_lst[0] in item and combi_lst[1] in item and combi_lst[2] in item and combi_lst[3] in item:
                remove_index.append((item))
        return remove_index
    if len(combi_lst) == 3:
        double = -1
        remove_index =[]
        kleurcode = ['black','white','red','yellow','blue','green']
        for i in range(0,6):
            if feedback[kleurcode[i]] == 2:
                double = i
        for item in lst:
            if combi_lst[0] in item and combi_lst[1] in item and combi_lst[2] in item:
                if item.count(double) == 2:
                    remove_index.append((item))
        return remove_index
    if len(combi_lst) == 2:
        remove_index =[]
        kleurcode = ['black','white','red','yellow','blue','green']
        for i in range(0,6):
            if feedback[kleurcode[i]] == 2:
                for item in lst:
                    if combi_lst[0] in item and combi_lst[1] in item:
                        if item.count(combi_lst[0]) == 2 and item.count(combi_lst[1]) == 2:
                            remove_index.append((item))
            elif feedback[kleurcode[i]] == 3:
                for item in lst:
                    if combi_lst[0] in item and combi_lst[1] in item:
                        if item.count(combi_lst[i]) == 3:
                            remove_index.append((item))

        return remove_index

def possible_combinations(code):
    """

    @param code:
    @return:
    """
    valid_chars = code
    all_combinations = (list(itertools.product(valid_chars, repeat=4)))  # <= list with tuples of 4 ('B', 'B', 'B', 'B')
    all_combinations = [list(i) for i in all_combinations]
    return all_combinations


all_combs = possible_combinations([0, 1, 2, 3, 4, 5])
code = all_combs[random.randint(0, len(all_combs))]
print(code)
for i in range(0, 11):
    if i == 0:
        print(
            f'======================================== Round {i + 1} ======================================================')
        givefeedback(code, simple_strat(i, feedback), feedback, f'round_{str(i)}')
    elif i == 10:
        print("U heeft de code niet geraden, volgende keer beter :D")
        break
    else:
        if feedback[f"round_{str(i - 1)}"]["black_pins"] != 4:
            print(f'======================================== Round {i + 1} ======================================================')
            givefeedback(code, simple_strat(i, feedback), feedback, f'round_{str(i)}')
        else:
            print("Gefeliciteerd u heeft de code goed geraden!!")
            break
