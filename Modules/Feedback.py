def givefeedback(og_code:list,gen_code:list,feedback:dict,round:str):
    whitepin_given = []
    blackpin_given = [100,100,100,100]
    for i in range(0,len(gen_code)):
        if gen_code[i] == og_code[i]:
            feedback[round]['black_pins']+=1
            blackpin_given.append(i)
            blackpin_given[i]=gen_code[i]
    if len(blackpin_given) == 4:    #check if any blackpins are added or not, if not the code 100 is added so the of statment down below works
        blackpin_given.append(100)
    for i in range(0, len(gen_code)):
        if gen_code[i] in og_code and (i not in blackpin_given[4:]and gen_code[i] not in blackpin_given[:4]):
            feedback[round]['white_pins'] += 1
            whitepin_given.append(i)
    feedback[round]['old_code']=gen_code
    return feedback