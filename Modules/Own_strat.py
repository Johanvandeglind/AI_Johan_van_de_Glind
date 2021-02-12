from Feedback import givefeedback
from base_codes import gues_code,all_equal,possible_combinations

def eigen_strat(round: int, feedback: dict):
    """
    Dit algoritme probeert eerst kleur voor kleur als combinatie, dus 4x zwart bijvoorbeeld.
    Dit doet hij net zo lang tot er een aantal van 4 zwarte pinnetjes is gegeven, dus bij de combinatie zwart zwart wit blauw,
    is de zwarte pin combinate 2,1,1, bij elkaar opgeteld is dat dus 4.

    @param round: Welke ronde de game is
    @param feedback: Def eedback die is gegeven voor elke ronde
    @return: nieuwe code om mee te raden
    """
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
            if black_pins < 4 and round != 0 and round < 7:
                return [round, round, round, round]
            else:
                return gues_code(round,feedback)
        else:
            return gues_code(round, feedback)



# Test script to test succes rate of code

# Test script to test succes rate of code
def play_hard():
    """
    Voert het spel uit mewt mijn eigen algoritme
    """
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
            givefeedback(code, eigen_strat(i, feedback), feedback, f'round_{str(i)}')
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
                givefeedback(code, eigen_strat(i, feedback), feedback, f'round_{str(i)}')

#     print(f"de totaal succes rondes = {len(succes)}")
#     count_rounds = dict(round_0=0,round_1=0,round_2=0,round_3=0,round_4=0,round_5=0,round_6=0,round_7=0,round_8=0,round_9=0)
#     for item in succes:
#         print(item)
#         count_rounds[f"round_{item}"] +=1
# # for i in range(0,10):
# #     count_rounds[f"round_{str(i)}"] = count_rounds[f"round_{i}"] /10000
#     print(count_rounds)