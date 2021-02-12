import itertools
import random

def gues_code(round:int,feedback:dict):
    """
    Gives code from list to feedback module and removes last guesed codes
    @param round: what round the game is in
    @param feedback: feedback dict with old codes and results
    @return: next gues code
    """
    right_color_lst = check_right_colors(feedback)
    lst = possible_combinations(right_color_lst)
    lst = remove_doubles_code_lst(lst, right_color_lst, feedback)
    for i in range(0, round-1):
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

def remove_doubles_code_lst(lst: list, combi_lst: list, feedback: dict):
    """
    Removes al double combinations, also removes the combinations that are not possible with the given feedback
    @param lst: List with all possible combinations
    @param combi_lst: The right numbers that are
    @param feedback:
    @return: list wothout doubles of all combinations
    """
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
    Makes a list of all possible combinatiens with give numbers
    @param code:the numbers that the list has to contain
    @return:the list of al combinations
    """
    valid_chars = code
    all_combinations = (list(itertools.product(valid_chars, repeat=4)))  # <= list with tuples of 4 ('B', 'B', 'B', 'B')
    all_combinations = [list(i) for i in all_combinations]
    return all_combinations

def check_right_colors(feedback: dict):
    """
    Checks all colours with black pins in feedback. and makes a list of the colours in the correct combination
    @param feedback: Feedback from feedback function
    @return: List with correct coloursw of combination
    """
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

