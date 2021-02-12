from Feedback import givefeedback
import random
from base_codes import gues_code, all_equal, possible_combinations


def simpel_code(round: int, feedback: dict):
    """
    Deze funcite probeerd de simple algorithm te implementeren maar dit lukt niet altijd.

    Ik loop vast op een punt wat ik ook in de opmerking bij het inleveren heb gedaan.
    @param round: actuele ronde
    @param feedback: de tot nu toe gegeven feeedback
    @return: nieuwe code om mee te raden.
    """
    if round == 0:
        all_combs = possible_combinations([0, 1, 2, 3, 4, 5])
        all_combs = sorted(all_combs)
        feedback["lst"] = all_combs
        return all_combs[0]
    else:
        fb = [0, 0]
        fb[0] = feedback[f"round_{round - 1}"]["black_pins"]
        fb[1] = feedback[f"round_{round - 1}"]["white_pins"]
        #print(fb)

        if fb == [0, 0]:
            colours = [0, 1, 2, 3, 4, 5]
            for item in colours:
                if item in feedback[f"round_{round - 1}"]["old_code"]:
                    colours.remove(item)
                #print(colours)
            all_combs = possible_combinations(colours)
            # all_combs = sorted(all_combs)
            feedback["lst"] = all_combs
            return all_combs[0]

        elif fb == [2, 2] or fb == [1, 3] or fb == [0, 4]:
            if feedback["lst"] == 0:
                colours = [0, 1, 2, 3, 4, 5]
                for item in colours:
                    if item not in feedback[f"round_{round - 1}"]["old_code"]:
                        colours.remove(item)
                        print(colours)
                all_combs = possible_combinations(colours)
                # all_combs = sorted(all_combs)
                feedback["lst"] = all_combs
                return all_combs[0]
            else:
                all_combs = feedback["lst"][1:]
                return all_combs[0]
        else:
            if fb != [0,3]:
                old_code = feedback[f"round_{round - 1}"]["old_code"]
                result = reduce(possible_combinations([0,1,2,3,4,5]),old_code,fb)
                feedback["lst"] = result
                return result[0]
            else:
                result = feedback["lst"]
                return result[-1]

def reduce(possible_combinations,code,score):
    """
    Zet alle combinaties in een lijst die dezrflde feedback krijgen als de zojuist geprobeerde combinatie
    @param possible_combinations: Alles combinaties
    @param code: Vorige code
    @param score: Feedback
    @return: Lijst met comobinaties
    """
    result = []

    for pos in possible_combinations:
        if score == feeedback_2(pos, code):
            result.append(pos)
    return result


def feeedback_2(code, secret):
    score = [0, 0]
    used = []
    for pos in range(len(code)):
        if code[pos] == secret[pos]:
            score[0] += 1
            used.append(pos)
    secret_copy = secret[::]
    for pos in used:
        secret_copy.remove(secret[pos])
    for i in range(len(code)):
        if i not in used:
            if code[i] in secret_copy:
                score[1] += 1
                secret_copy.remove(code[i])

    return score


def play_medium():
    """
    voort het spel uit met de simpel strategie
    """
    succes = []
    #for x in range(0, 2):
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
            givefeedback(code, simpel_code(i, feedback), feedback, f'round_{str(i)}')
        elif i == 10:
            print("U heeft gewonnen! De computer heeft de code geraden")
            #print(f"Het aantal succesen op {x+1} aantal keer proberen is: {succes}")
            break
        elif i==9 and feedback[f"round_{str(i - 1)}"]["black_pins"] == 4:
            print("De computer heeft de code geraden")
            succes.append(i)
        #print(f"Het aantal succesen op {x+1} aantal keer proberen is: {succes}")
            break
        else:
            if feedback[f"round_{str(i - 1)}"]["black_pins"] == 4:
                print("De computer heeft de code geraden")
                succes.append(i)
                #print(f"Het aantal succesen op {x+1} aantal keer proberen is: {succes}")
                break

            else:
                #print(f'======================================== Round {i + 1} ======================================================')
                givefeedback(code, simpel_code(i, feedback), feedback, f'round_{str(i)}')


#     print(f"de totaal succes rondes = {len(succes)}")
#     count_rounds = dict(round_0=0,round_1=0,round_2=0,round_3=0,round_4=0,round_5=0,round_6=0,round_7=0,round_8=0,round_9=0)
#     for item in succes:
#         print(item)
#         count_rounds[f"round_{item}"] +=1
# # for i in range(0,10):
# #     count_rounds[f"round_{str(i)}"] = count_rounds[f"round_{i}"] /10000
#     print(count_rounds)
