import itertools
import random
from Feedback import givefeedback


def eigen_strat(round: int, feedback: dict):
    """
    @param round:
    @param feedback:
    @return:
    """

    # print(feedback["black"],feedback["white"],feedback["red"],feedback["yellow"],feedback["blue"],feedback["green"])

    if round == 0:
        return [round, round, round, round]
    elif feedback[f"round_{round - 1}"]["black_pins"] == 4:
        return feedback[f"round_{round - 1}"]["old_code"]
    else:
        if len(feedback["lst"])==0:
            black_pins = 0
            colour_lst = ["black", "white", "red", "yellow", "blue", "green"]
            if all_equal(feedback[f"round_{str(round-1)}"]["old_code"]):
                feedback[colour_lst[round - 1]] = feedback[f"round_{round - 1}"]["black_pins"]
            for item in range(0, round):
                black_pins = black_pins + feedback[f"round_{str(item)}"]["black_pins"]
                #print(feedback[f"round_{str(item)}"]["black_pins"])
            if black_pins < 4 and round != 0 and round < 7:
                #print(feedback[f"round_{round - 1}"]["black_pins"])
                #print([round, round, round, round])
                return [round, round, round, round]
            else:
                return gues_code(round,feedback)
        else:
            return gues_code(round, feedback)



def gues_code(round:int,feedback:dict):
    right_color_lst = check_right_colors(feedback)
    lst = possible_combinations(right_color_lst)
    lst = remove_doubles_code_lst(lst, right_color_lst, feedback)
    for i in range(0, round):
        if feedback[f"round_{i}"]["old_code"] in lst:
            old_code = feedback[f"round_{i}"]["old_code"]
            lst.remove(old_code)
    feedback["lst"] = lst
    #(lst)
    code = lst[random.randint(0, len(lst) - 1)]
    #print(code)
    return code


def all_equal(lst):
    return all(lst[0]==i for i in lst)
def check_right_colors(feedback: dict):
    combi_lst = []
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


def remove_doubles_code_lst(lst: list, combi_lst: list, feedback: dict):
    if len(combi_lst) == 4:
        remove_index = []
        for item in lst:
            if combi_lst[0] in item and combi_lst[1] in item and combi_lst[2] in item and combi_lst[3] in item:
                remove_index.append((item))
        return remove_index
    if len(combi_lst) == 3:
        double = -1
        remove_index = []
        kleurcode = ['black', 'white', 'red', 'yellow', 'blue', 'green']
        for i in range(0, 6):
            if feedback[kleurcode[i]] == 2:
                double = i
        for item in lst:
            if combi_lst[0] in item and combi_lst[1] in item and combi_lst[2] in item:
                if item.count(double) == 2:
                    remove_index.append((item))
        return remove_index
    if len(combi_lst) == 2:
        remove_index = []
        kleurcode = ['black', 'white', 'red', 'yellow', 'blue', 'green']
        for i in range(0, 6):
            if feedback[kleurcode[i]] == 2:
                for item in lst:
                    if combi_lst[0] in item and combi_lst[1] in item:
                        if item.count(combi_lst[0]) == 2 and item.count(combi_lst[1]) == 2:
                            remove_index.append((item))
            elif feedback[kleurcode[i]] == 3:
                for item in lst:
                    if combi_lst[0] in item and combi_lst[1] in item:
                        if item.count(i) == 3:
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


succes = 0
for x in range(0, 1296):
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
                    green=0,
                    lst=[]
                    )
    all_combs = possible_combinations([0, 1, 2, 3, 4, 5])
    code = all_combs[x]

    # code = [4, 2, 4, 2]
    #print(code)
    for i in range(0, 11):
        if i == 0:
            #print(f'======================================== Round {i + 1} ======================================================')
            givefeedback(code, eigen_strat(i, feedback), feedback, f'round_{str(i)}')
        elif i == 10:
            #print("U heeft de code niet geraden, volgende keer beter :D")
            print(f"Het aantal succesen op {x+1} aantal keer proberen is: {succes}")
            break
        elif i==9 and feedback[f"round_{str(i - 1)}"]["black_pins"] == 4:
            #print("Gefeliciteerd u heeft de code goed geraden!!")
            succes += 1
            print(f"Het aantal succesen op {x+1} aantal keer proberen is: {succes}")
            break
        else:
            if feedback[f"round_{str(i - 1)}"]["black_pins"] == 4:
                #print("Gefeliciteerd u heeft de code goed geraden!!")
                succes += 1
                print(f"Het aantal succesen op {x+1} aantal keer proberen is: {succes}")
                break

            else:
                #print(f'======================================== Round {i + 1} ======================================================')
                givefeedback(code, eigen_strat(i, feedback), feedback, f'round_{str(i)}')


print(f"Het succes persentage = {100/1296*succes}%")
