from Random_strategie import play_easy
from Simple_Strategie import play_medium
from Own_strat import play_hard
from user_against_computer import game_player_gueses


spelvorm = str(input('Welke sple vor wilt us spelen?\na: U raad de code van de computer\nb: de Computer raad uw code\n'))
if spelvorm == 'a':
    game_player_gueses()
else:
    diff = str(input('Welke difficulty wilt u:\na: Easy\nb: Medium\nc: Hard\n'))
    if diff == 'a':
        play_easy()
    elif diff == 'b':
        play_medium()
    elif diff == 'c':
        play_hard()