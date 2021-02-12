from Feedback import givefeedback
import random
from base_codes import gues_code,all_equal,possible_combinations

def random_code(round:int,feedback:dict):
    """
    Pakt of maakt een lijst en kiest hier random een functie uit
    @param round:
    @param feedback:
    @return:
    """
    if round == 0:
        all_combs = possible_combinations([0, 1, 2, 3, 4, 5])
        return all_combs[random.randint(0,len(all_combs)-1)]
    if round >0:
        all_combs = possible_combinations([0, 1, 2, 3, 4, 5])
        for i in range(0, round):
            if feedback[f"round_{i}"]["old_code"] in all_combs:
                old_code = feedback[f"round_{i}"]["old_code"]
                all_combs.remove(old_code)
        return all_combs[random.randint(0,len(all_combs)-1)]

def play_easy():
    succes = []

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
    #code = all_combs[random.randint(0,len(all_combs)-1)]
    code = list(input(f'Wat zijn de kleuren, maak een keuze uit deze 6 kleuren (geef zo 1234 uw nummers op):\n0:Zwart\n1:Wit\n2:Rood\n3:Geel\n4:Blauw\n5:Groen\n'))

    # code = [4, 2, 4, 2]
    #print(code)
    for i in range(0, 11):
        if i == 0:
            #print(f'======================================== Round {i + 1} ======================================================')
            givefeedback(code, random_code(i, feedback), feedback, f'round_{str(i)}')
        elif i == 10:
            print("U heeft gewonnen! De computer heeft de code geraden")
                # print(f"Het aantal succesen op {x+1} aantal keer proberen is: {succes}")
            break
        elif i == 9 and feedback[f"round_{str(i - 1)}"]["black_pins"] == 4:
            print("De computer heeft de code geraden")
            succes.append(i)
                # print(f"Het aantal succesen op {x+1} aantal keer proberen is: {succes}")
            break
        else:
            if feedback[f"round_{str(i - 1)}"]["black_pins"] == 4:
                print("De computer heeft de code geraden")
                succes.append(i)
                # print(f"Het aantal succesen op {x+1} aantal keer proberen is: {succes}")
                break

            else:
                #print(f'======================================== Round {i + 1} ======================================================')
                givefeedback(code, random_code(i, feedback), feedback, f'round_{str(i)}')

#     print(f"de totaal succes rondes = {len(succes)}")
#     count_rounds = dict(round_0=0,round_1=0,round_2=0,round_3=0,round_4=0,round_5=0,round_6=0,round_7=0,round_8=0,round_9=0)
#     for item in succes:
#         print(item)
#         count_rounds[f"round_{item}"] +=1
# # for i in range(0,10):
# #     count_rounds[f"round_{str(i)}"] = count_rounds[f"round_{i}"] /10000
#     print(count_rounds)