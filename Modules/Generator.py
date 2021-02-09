from random import randint
from Feedback import givefeedback

def Generate(feedback:dict,round:str,):
    code = [0,0,0,0]
    old_code = feedback['round_0']['old_code']
    if round == 'round_0':
        for i in range(0,4):
                code[i] = randint(0,5)
        print(code)
        return code
    #if round == 'round_1':
        #for i in range(0,feedback['round_0']['black_pins']):
    #return code



def game_player_gueses():
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
    code = Generate(feedback, 'round_0')
    for i in range(0,11):
        if i == 0:
            print(f'======================================== Round {i+1} ======================================================')
            givefeedback(code,raad_code_user(feedback,i),feedback,f'round_{str(i)}' )
        elif i == 10:
            print("U heeft de code niet geraden, volgende keer beter :D")
            break
        else:
            if feedback[f"round_{str(i-1)}"]["black_pins"] != 4:
                print(f'======================================== Round {i+1} ======================================================')
                givefeedback(code,raad_code_user(feedback,i),feedback,f'round_{str(i)}' )
            else:
                print("Gefeliciteerd u heeft de code goed geraden!!")
                break


def raad_code_user(feedback:dict,round:int):
    '''

    '''
    if round == 0:
        inp_code= user_color_code()
    elif round == 9:
        print('Dit is uw laatste kans')
        print("-----------------------------------------------------------------------------------------------")
        for i in range(0, round):
            uitschfijven_feedback(round,i,feedback)
        inp_code= user_color_code()
    else:
        print("-----------------------------------------------------------------------------------------------")
        for i in range(0,round):
            uitschfijven_feedback(round, i, feedback)
        inp_code =user_color_code()
    return inp_code



def uitschfijven_feedback(round:int,i:int,feedback:dict):
    kleuren_combi = ['Zwart', 'Wit', 'Rood', 'Geel', 'Blauw', 'Groen']
    for i in range(0, round):
        print(f'Feedback {i + 1}e ronde:\n'
              f'Uw code was:{kleuren_combi[feedback[f"round_{round - 1}"]["old_code"][0]]} {kleuren_combi[feedback[f"round_{round - 1}"]["old_code"][1]]} {kleuren_combi[feedback[f"round_{round - 1}"]["old_code"][2]]} {kleuren_combi[feedback[f"round_{round - 1}"]["old_code"][3]]}\n'
              f'Zwarte pinnejtes:{feedback[f"round_{round - 1}"]["black_pins"]}\n'
              f'Witte pinnejtes:{feedback[f"round_{round - 1}"]["white_pins"]}')
        print("-----------------------------------------------------------------------------------------------")

def user_color_code():
    '''
    Fucntie voor het invoeren van de code van user (raden of bij het starten)
    '''
    inp_code = []
    kleuren = ['1:Zwart', '2:Wit', '3:Rood', '4:Geel', '5:Blauw', '6:Groen']
    for i in range(0, 4):
        inp_code.append(int(input(
            f'Wat is de {i + 1}e kleur, maak een keuze uit deze 6 kleuren (geef uw nummer op):\n1:Zwart\n2:Wit\n3:Rood\n4:Geel\n5:Blauw\n6:Groen\n')) - 1)
        print(f'Uw keuze was {kleuren[inp_code[i]]}')
    return inp_code


game_player_gueses()