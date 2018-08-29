from uarm.wrapper import SwiftAPI













def jouer_bleu(pion, case) :

#if case != ('A1')&('A2')&('A3')&('B1')&('B2')&('B3')&('C1')&('C2')&('C3') :
#    print('case incorect')    


    if pion == 'R1' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(115, -115, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(115, -115, 0)
        swift.flush_cmd(wait_stop=True)
        swift.set_pump(on=True)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(115, -115, 50)
    elif pion == 'R2' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(155, -115, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(155, -115, 0)
        swift.flush_cmd(wait_stop=True)
        swift.set_pump(on=True)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(155, -115, 50)
    elif pion == 'R3' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(195, -115, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(195, -115, 0)
        swift.flush_cmd(wait_stop=True)
        swift.set_pump(on=True)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(195, -115, 50)
    elif pion == 'R4' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(235, -115, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(235, -115, 0)
        swift.flush_cmd(wait_stop=True)
        swift.set_pump(on=True)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(235, -115, 50)
    elif pion == 'R5' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(270, -115, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(270, -115, 0)
        swift.flush_cmd(wait_stop=True)
        swift.set_pump(on=True)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(270, -115, 50)
    else :
        print('numéro incorect')

    if case == 'A1' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'A2' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'A3' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'B1' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 0, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'B2' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 0, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'B3' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 0, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'C1' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, -55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'C2' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, -55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'C3' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, -55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)

        return



def jouer_rouge(pion, case) :

#if case != ('A1')&('A2')&('A3')&('B1')&('B2')&('B3')&('C1')&('C2')&('C3') :
#    print('case incorect')    


    if pion == 'L1' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(115, 120, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(115, 120, 0)
        swift.flush_cmd(wait_stop=True)
        swift.set_pump(on=True)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(115, 120, 50)
    elif pion == 'L2' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(155, 120, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(155, 120, 0)
        swift.flush_cmd(wait_stop=True)
        swift.set_pump(on=True)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(155, 120, 50)
    elif pion == 'L3' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(195, 120, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(195, 120, 0)
        swift.flush_cmd(wait_stop=True)
        swift.set_pump(on=True)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(195, 120, 50)
    elif pion == 'L4' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(235, 120, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(235, 120, 0)
        swift.flush_cmd(wait_stop=True)
        swift.set_pump(on=True)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(235, 120, 50)
    elif pion == 'L5' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(270, 120, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(270, 120, 0)
        swift.flush_cmd(wait_stop=True)
        swift.set_pump(on=True)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(270, 120, 50)
    else :
        print('numéro incorect')

    if case == 'A1' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'A2' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'A3' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'B1' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 0, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'B2' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 0, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'B3' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 0, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, 0, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'C1' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, -55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(170, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'C2' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, -55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(220, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)
    elif case == 'C3' :
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, -55, 0)
        swift.set_pump(on=False)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(275, -55, 50)
        swift.flush_cmd(wait_stop=True)
        swift.set_position(150, 0, 50)

        return

swift = SwiftAPI()
swift.set_speed_factor(2)

first = input('couleur du joueur jouant en premier : ')
if first == 'bleu' :
    print("ROUND 1")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case1=case
    jouer_bleu(pion, case)

    print("ROUND 2")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case2=case
    if case == case1 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_rouge(pion, case)

    print("ROUND 3")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case3=case
    if case == case1 or case2:
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_bleu(pion, case)

    print("ROUND 4")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case4=case
    if case == case1 or case2 or case3 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_rouge(pion, case)

    print("ROUND 5")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case5=case
    if case == case1 or case2 or case3 or case4 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_bleu(pion, case)

    print("ROUND 6")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case6=case
    if case == case1 or case2 or case3 or case4 or case5 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_rouge(pion, case)

    print("ROUND 7")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case7=case
    if case == case1 or case2 or case3 or case4 or case5 or case6 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_bleu(pion, case)

    print("ROUND 8")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case8=case
    if case == case1 or case2 or case3 or case4 or case5 or case6 or case7 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_rouge(pion, case)

    print("ROUND 9")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    if case == case1 or case2 or case3 or case4 or case5 or case6 or case7 or case8 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_bleu(pion, case)
