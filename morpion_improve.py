def jouer_bleu(pion, case) :

#if case != ('A1')&('A2')&('A3')&('B1')&('B2')&('B3')&('C1')&('C2')&('C3') :
#    print('case incorect')    


    if pion == 'R1' :
        swift.set_position(115, -115, 50, wait=True)
        swift.set_position(115, -115, 0, wait=True)
        swift.set_pump(on=True)
        swift.set_position(115, -115, 50, wait=True)
    elif pion == 'R2' :
        swift.set_position(155, -115, 50, wait=True)
        swift.set_position(155, -115, 0, wait=True)
        swift.set_pump(on=True)
        swift.set_position(155, -115, 50, wait=True)
    elif pion == 'R3' :
        swift.set_position(195, -115, 50, wait=True)
        swift.set_position(195, -115, 0, wait=True)
        swift.set_pump(on=True)
        swift.set_position(195, -115, 50, wait=True)
    elif pion == 'R4' :
        swift.set_position(235, -115, 50, wait=True)
        swift.set_position(235, -115, 0, wait=True)
        swift.set_pump(on=True)
        swift.set_position(235, -115, 50, wait=True)
    elif pion == 'R5' :
        swift.set_position(270, -115, 50, wait=True)
        swift.set_position(270, -115, 0, wait=True)
        swift.set_pump(on=True)
        swift.set_position(270, -115, 50, wait=True)
    else :
        print('numéro incorect')

    if case == 'A1' :
        swift.set_position(170, 55, 50, wait=True)
        swift.set_position(170, 55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(170, 55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'A2' :
        swift.set_position(220, 55, 50, wait=True)
        swift.set_position(220, 55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(220, 55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'A3' :
        swift.set_position(275, 55, 50, wait=True)
        swift.set_position(275, 55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(275, 55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'B1' :
        swift.set_position(170, 0, 50, wait=True)
        swift.set_position(170, 0, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(170, 0, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'B2' :
        swift.set_position(220, 0, 50, wait=True)
        swift.set_position(220, 0, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(220, 0, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'B3' :
        swift.set_position(275, 0, 50, wait=True)
        swift.set_position(275, 0, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(275, 0, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'C1' :
        swift.set_position(170, -55, 50, wait=True)
        swift.set_position(170, -55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(170, -55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'C2' :
        swift.set_position(220, -55, 50, wait=True)
        swift.set_position(220, -55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(220, -55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'C3' :
        swift.set_position(275, -55, 50, wait=True)
        swift.set_position(275, -55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(275, -55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)

        return



def jouer_rouge(pion, case) :  


    if pion == 'L1' :
        swift.set_position(115, 120, 50, wait=True)
        swift.set_position(115, 120, 0, wait=True)
        swift.set_pump(on=True)
        swift.set_position(115, 120, 50, wait=True)
    elif pion == 'L2' :
        swift.set_position(155, 120, 50, wait=True)
        swift.set_position(155, 120, 0, wait=True)
        swift.set_pump(on=True)
        swift.set_position(155, 120, 50, wait=True)
    elif pion == 'L3' :
        swift.set_position(195, 120, 50, wait=True)
        swift.set_position(195, 120, 0, wait=True)
        swift.set_pump(on=True)
        swift.set_position(195, 120, 50, wait=True)
    elif pion == 'L4' :
        swift.set_position(235, 120, 50, wait=True)
        swift.set_position(235, 120, 0, wait=True)
        swift.set_pump(on=True)
        swift.set_position(235, 120, 50, wait=True)
    elif pion == 'L5' :
        swift.set_position(270, 120, 50, wait=True)
        swift.set_position(270, 120, 0, wait=True)
        swift.set_pump(on=True)
        swift.set_position(270, 120, 50, wait=True)
    else :
        print('numéro incorect')

    if case == 'A1' :
        swift.set_position(170, 55, 50, wait=True)
        swift.set_position(170, 55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(170, 55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'A2' :
        swift.set_position(220, 55, 50, wait=True)
        swift.set_position(220, 55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(220, 55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'A3' :
        swift.set_position(275, 55, 50, wait=True)
        swift.set_position(275, 55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(275, 55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'B1' :
        swift.set_position(170, 0, 50, wait=True)
        swift.set_position(170, 0, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(170, 0, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'B2' :
        swift.set_position(220, 0, 50, wait=True)
        swift.set_position(220, 0, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(220, 0, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'B3' :
        swift.set_position(275, 0, 50, wait=True)
        swift.set_position(275, 0, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(275, 0, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'C1' :
        swift.set_position(170, -55, 50, wait=True)
        swift.set_position(170, -55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(170, -55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'C2' :
        swift.set_position(220, -55, 50, wait=True)
        swift.set_position(220, -55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(220, -55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
    elif case == 'C3' :
        swift.set_position(275, -55, 50, wait=True)
        swift.set_position(275, -55, 0, wait=True)
        swift.set_pump(on=False)
        swift.set_position(275, -55, 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)

        return

def first_bleu() :
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

    return


def first_rouge() :
    print("ROUND 1")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case1=case
    jouer_rouge(pion, case)

    print("ROUND 2")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case2=case
    if case == case1 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_bleu(pion, case)

    print("ROUND 3")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case3=case
    if case == case1 or case2:
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_rouge(pion, case)

    print("ROUND 4")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case4=case
    if case == case1 or case2 or case3 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_bleu(pion, case)

    print("ROUND 5")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case5=case
    if case == case1 or case2 or case3 or case4 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_rouge(pion, case)

    print("ROUND 6")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case6=case
    if case == case1 or case2 or case3 or case4 or case5 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_bleu(pion, case)

    print("ROUND 7")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case7=case
    if case == case1 or case2 or case3 or case4 or case5 or case6 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_rouge(pion, case)

    print("ROUND 8")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    case8=case
    if case == case1 or case2 or case3 or case4 or case5 or case6 or case7 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_bleu(pion, case)

    print("ROUND 9")
    pion = input('numéro du pion voulant etre déplacé : ')
    case = input('case ou le pion doit etre posé : ')
    if case == case1 or case2 or case3 or case4 or case5 or case6 or case7 or case8 :
        print('Case deja occupé, veuillez en choisir une autre')
    else :
        jouer_rouge(pion, case)

    return






from uarm.wrapper import SwiftAPI
swift = SwiftAPI()
swift.set_speed_factor(2)
swift.waiting_ready()
#swift.set_position(120, 0, 50)
first = input('couleur du joueur jouant en premier : ')
if first == 'bleu' :
    first_bleu()
else :
    first=rouge()

