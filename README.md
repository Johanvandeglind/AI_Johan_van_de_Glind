# Mastermind setup:
![](images/mastermind.jpg)

---    
###	Main programma: communicatie met user met keuze menu uit 4 spel vorm opties
####	Keuze 1: Computer tegen speler
    Invoer user combinatie
    Computer raad fucntie
        Reageren op feedback
        Maximaal 10 probeersels
    Feedback module user Zwarte pinnetjes
    Feedback user witte pinnetjes
####	Keuze 2: Tegen computer spelen speler raad
	Functie voor bedenken code van computer
	Feedback functie van computer
---------
### Modules
#### Strategies
#### Own Algorithm
    Dit algoritme probeert eerst kleur voor kleur als combinatie, dus 4x zwart bijvoorbeeld.
    Dit doet hij net zo lang tot er een aantal van 4 zwarte pinnetjes is gegeven, dus bij de combinatie zwart zwart wit blauw,
    is de zwarte pin combinate 2,1,1, bij elkaar opgeteld is dat dus 4.
##### Simpel strategie
    A Simple Strategy
    The first strategy by Shapiro (Shapiro, 1983) (it is also published in (Sterling and Shapiro, 1994)). His
    algorithm does is the following: the combinations are somehow ordered (usually alphabetically) and the
    first combination is asked. The answer is received. The next question is the first one in the ordering that is
    consistent with the answers given so far. And so on until the combination is cracked. A crucial drawback
    to this strategy, however, is that it looks at the informativity of questions very marginally. One can only be
    certain that one does not know the answer already, but that is all.
##### Random strat
    Pakt of maakt een lijst en kiest hier random een functie uit

#### Gamemodes
##### Player against computer (computer make code and player gueses) 
    Speler raad de code van de computer
##### Computer against player (Player gueses)
    Computer raad code van speler
#### Base functions
    verschillende fucnties die in meerdere gevallen toepasbaar zijn.
    Gues_codde():
    Deze fucntie zorgt voor een nieuwe code als de juiste kleuren bekend zijn.
    
    all_equal():
    zorgd ervoor dat de code lijsten geen absolute dubbelen bevat
    
    remove_doubles_code_lst():
    zorgd ervoor dat als de kleuren die in de secret zitten bekend zijn er een lijst komt met alleen di kleuren.
    
    possible_combinations():
    Genereert lijst met alle combinaties van opgegeven kleuren
    
    check_right_colors():
    Kijkt welke kleuren samen 4 zwarte pinnetjes geven

---------
#### bron vermelding
    Boss, R. (2021, 19 januari). HU Structured Programming - Mastermind. Youtube. https://www.youtube.com/watch?v=rSzX2TtjvHA&feature=youtu.be
    Paper groningen universiteit: 
    Kooi, B. (2005). YET ANOTHER MASTERMIND STRATEGY. ICGA Journal, 28(1), 13–20. https://doi.org/10.3233/icg-2005-28105
#### libraries
    random    
    itertools