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
                round_9=dict(black_pins=0, white_pins=0, old_code=[0, 0, 0, 0])
                )

def simple_strat(round:int,feedback:dict):
    print(feedback)
    code=[]
    if round == 0:
        code = [0, 1, 2, 3]
        return code
    if round == 1:
        if feedback["round_0"]["white_pins"] == 4:
            possible_combinations(feedback["round_0"]["old_code"])
        elif feedback["round_0"]["white_pins"] == 0:
            code = possible_combinations([4,5])[random.randint(0,len(possible_combinations))]
    return code



def possible_combinations(code):
    valid_chars = code
    all_combinations = (list(itertools.product(valid_chars, repeat=4)))  # <= list with tuples of 4 ('B', 'B', 'B', 'B')
    all_combinations = [list(i) for i in all_combinations]
    return all_combinations


all_combs = possible_combinations([0,1,2,3,4,5])
code = all_combs[random.randint(0,len(all_combs))]


for i in range(0, 3):
    if i == 0:
        print(f'======================================== Round {i + 1} ======================================================')
        givefeedback(code, simple_strat( i,feedback), feedback, f'round_{str(i)}')
    else:
        if feedback[f"round_{str(i - 1)}"]["black_pins"] != 4:
            print(f'======================================== Round {i + 1} ======================================================')
            givefeedback(code, simple_strat( i,feedback), feedback, f'round_{str(i)}')
        else:
            print("Gefeliciteerd u heeft de code goed geraden!!")
            break
