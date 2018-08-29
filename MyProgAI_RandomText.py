#!/usr/bin/python

import random
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
lignes = 3
colonnes = 3
global lst
global color
color = "yellow"
lst = [[0]*colonnes for _ in range(lignes)]


CAS1 = 0
CAS2 = 0
CAS3 = 0
CAS4 = 0

def extraire(line) :
   case = line.strip('\n')
   case = case.split(";")
   return(case)


fichier = open("coordonnes.txt", "r")

r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
a1 = []
a2 = []
a3 = []
b1 = []
b2 = []
b3 = []
c1 = []
c2 = []
c3 = []
   
r1 = fichier.readline()
r2 = fichier.readline()
r3 = fichier.readline()
r4 = fichier.readline()
r5 = fichier.readline()

l1 = fichier.readline()
l2 = fichier.readline()
l3 = fichier.readline()
l4 = fichier.readline()
l5 = fichier.readline()

a1 = fichier.readline()
a2 = fichier.readline()
a3 = fichier.readline()
b1 = fichier.readline()
b2 = fichier.readline()
b3 = fichier.readline()
c1 = fichier.readline()
c2 = fichier.readline()
c3 = fichier.readline()

fichier.close()

R1 = extraire(r1)
R2 = extraire(r2)
R3 = extraire(r3)
R4 = extraire(r4)
R5 = extraire(r5)
L1 = extraire(l1)
L2 = extraire(l2)
L3 = extraire(l3)
L4 = extraire(l4)
L5 = extraire(l5)
A1 = extraire(a1)
A2 = extraire(a2)
A3 = extraire(a3)
B1 = extraire(b1)
B2 = extraire(b2)
B3 = extraire(b3)
C1 = extraire(c1)
C2 = extraire(c2)
C3 = extraire(c3)


def jouer_bleu(case, x) :
    if (x/2 == 0) :
        swift.set_position(int(R1[1]), int(R1[2]), 50, wait=True)
        swift.set_position(int(R1[1]), int(R1[2]), int(R1[3]), wait=True)
        swift.set_pump(on=True)
        swift.set_position(int(R1[1]), int(R1[2]), 50, wait=True)
    elif (x/2 == 1) :
        swift.set_position(int(R2[1]), int(R2[2]), 50, wait=True)
        swift.set_position(int(R2[1]), int(R2[2]), int(R2[3]), wait=True)
        swift.set_pump(on=True)
        swift.set_position(int(R2[1]), int(R2[2]), 50, wait=True)
    elif (x/2 == 2) :
        swift.set_position(int(R3[1]), int(R3[2]), 50, wait=True)
        swift.set_position(int(R3[1]), int(R3[2]), int(R3[3]), wait=True)
        swift.set_pump(on=True)
        swift.set_position(int(R3[1]), int(R3[2]), 50, wait=True)
    elif (x/2 == 3) :
        swift.set_position(int(R4[1]), int(R4[2]), 50, wait=True)
        swift.set_position(int(R4[1]), int(R4[2]), int(R4[3]), wait=True)
        swift.set_pump(on=True)
        swift.set_position(int(R4[1]), int(R4[2]), 50, wait=True)
    elif (x/2 == 4) :
        swift.set_position(int(R5[1]), int(R5[2]), 50, wait=True)
        swift.set_position(int(R5[1]), int(R5[2]), int(R5[3]), wait=True)
        swift.set_pump(on=True)
        swift.set_position(int(R5[1]), int(R5[2]), 50, wait=True)
        

    if case == 'A1' :
        swift.set_position(int(A1[1]), int(A1[2]), 50, wait=True)
        swift.set_position(int(A1[1]), int(A1[2]), int(A1[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(A1[1]), int(A1[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[0][2]=2
    elif case == 'A2' :
        swift.set_position(int(A2[1]), int(A2[2]), 50, wait=True)
        swift.set_position(int(A2[1]), int(A2[2]), int(A2[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(A2[1]), int(A2[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[0][1]=2
    elif case == 'A3' :
        swift.set_position(int(A3[1]), int(A3[2]), 50, wait=True)
        swift.set_position(int(A3[1]), int(A3[2]), int(A3[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(A3[1]), int(A3[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[0][0]=2
    elif case == 'B1' :
        swift.set_position(int(B1[1]), int(B1[2]), 50, wait=True)
        swift.set_position(int(B1[1]), int(B1[2]), int(B1[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(B1[1]), int(B1[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[1][2]=2
    elif case == 'B2' :
        swift.set_position(int(B2[1]), int(B2[2]), 50, wait=True)
        swift.set_position(int(B2[1]), int(B2[2]), int(B2[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(B2[1]), int(B2[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[1][1]=2
    elif case == 'B3' :
        swift.set_position(int(B3[1]), int(B3[2]), 50, wait=True)
        swift.set_position(int(B3[1]), int(B3[2]), int(B3[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(B3[1]), int(B3[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[1][0]=2
    elif case == 'C1' :
        swift.set_position(int(C1[1]), int(C1[2]), 50, wait=True)
        swift.set_position(int(C1[1]), int(C1[2]), int(C1[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(C1[1]), int(C1[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[2][2]=2
    elif case == 'C2' :
        swift.set_position(int(C2[1]), int(C2[2]), 50, wait=True)
        swift.set_position(int(C2[1]), int(C2[2]), int(C2[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(C2[1]), int(C2[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[2][1]=2
    elif case == 'C3' :
        swift.set_position(int(C3[1]), int(C3[2]), 50, wait=True)
        swift.set_position(int(C3[1]), int(C3[2]), int(C3[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(C3[1]), int(C3[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[2][0]=2

        return



def jouer_rouge(case, x, b) :
    if (((x+b)//2) == 0) :
        swift.set_position(int(L1[1]), int(L1[2]), 50, wait=True)
        swift.set_position(int(L1[1]), int(L1[2]), int(L1[3]), wait=True)
        swift.set_pump(on=True)
        swift.set_position(int(L1[1]), int(L1[2]), 50, wait=True)
    elif (((x+b)//2) == 1) :
        swift.set_position(int(L2[1]), int(L2[2]), 50, wait=True)
        swift.set_position(int(L2[1]), int(L2[2]), int(L2[3]), wait=True)
        swift.set_pump(on=True)
        swift.set_position(int(L2[1]), int(L2[2]), 50, wait=True)
    elif (((x+b)//2) == 2) :
        swift.set_position(int(L3[1]), int(L3[2]), 50, wait=True)
        swift.set_position(int(L3[1]), int(L3[2]), int(L3[3]), wait=True)
        swift.set_pump(on=True)
        swift.set_position(int(L3[1]), int(L3[2]), 50, wait=True)
    elif (((x+b)//2) == 3) :
        swift.set_position(int(L4[1]), int(L4[2]), 50, wait=True)
        swift.set_position(int(L4[1]), int(L4[2]), int(L4[3]), wait=True)
        swift.set_pump(on=True)
        swift.set_position(int(L4[1]), int(L4[2]), 50, wait=True)
    elif (((x+b)//2) == 4) :
        swift.set_position(int(L5[1]), int(L5[2]), 50, wait=True)
        swift.set_position(int(L5[1]), int(L5[2]), int(L5[3]), wait=True)
        swift.set_pump(on=True)
        swift.set_position(int(L5[1]), int(L5[2]), 50, wait=True)

    if case == 'A1' :
        swift.set_position(int(A1[1]), int(A1[2]), 50, wait=True)
        swift.set_position(int(A1[1]), int(A1[2]), int(A1[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(A1[1]), int(A1[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[0][2]=1
    elif case == 'A2' :
        swift.set_position(int(A2[1]), int(A2[2]), 50, wait=True)
        swift.set_position(int(A2[1]), int(A2[2]), int(A2[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(A2[1]), int(A2[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[0][1]=1
    elif case == 'A3' :
        swift.set_position(int(A3[1]), int(A3[2]), 50, wait=True)
        swift.set_position(int(A3[1]), int(A3[2]), int(A3[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(A3[1]), int(A3[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[0][0]=1
    elif case == 'B1' :
        swift.set_position(int(B1[1]), int(B1[2]), 50, wait=True)
        swift.set_position(int(B1[1]), int(B1[2]), int(B1[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(B1[1]), int(B1[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[1][2]=1
    elif case == 'B2' :
        swift.set_position(int(B2[1]), int(B2[2]), 50, wait=True)
        swift.set_position(int(B2[1]), int(B2[2]), int(B2[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(B2[1]), int(B2[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[1][1]=1
    elif case == 'B3' :
        swift.set_position(int(B3[1]), int(B3[2]), 50, wait=True)
        swift.set_position(int(B3[1]), int(B3[2]), int(B3[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(B3[1]), int(B3[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[1][0]=1
    elif case == 'C1' :
        swift.set_position(int(C1[1]), int(C1[2]), 50, wait=True)
        swift.set_position(int(C1[1]), int(C1[2]), int(C1[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(C1[1]), int(C1[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[2][2]=1
    elif case == 'C2' :
        swift.set_position(int(C2[1]), int(C2[2]), 50, wait=True)
        swift.set_position(int(C2[1]), int(C2[2]), int(C2[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(C2[1]), int(C2[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[2][1]=1
    elif case == 'C3' :
        swift.set_position(int(C3[1]), int(C3[2]), 50, wait=True)
        swift.set_position(int(C3[1]), int(C3[2]), int(C3[3]), wait=True)
        swift.set_pump(on=False)
        swift.set_position(int(C3[1]), int(C3[2]), 50, wait=True)
        swift.set_position(150, 0, 50, wait=True)
        lst[2][0]=1

        return


def place_A1() :
    global x
    global b
    global AI
    global k
    k = k + 1
    if (lst[0][2] == 1) or (lst[0][2] == 2) :
        warning()
        return
    if (x % 2 == 1) :
        bA1.config(image = red)
        bA1.image = red
        bA1.pack(ipady = 20, ipadx = 12)
        jouer_rouge("A1", x, b)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    else :
        bA1.config(image = blue)
        bA1.image = blue
        bA1.pack(ipady = 20, ipadx = 12)
        jouer_bleu("A1", x)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    if (x > 7) :
        draw()
        return
def place_A2() :
    global x
    global b
    global AI
    global k
    k = k + 1
    if (lst[0][1] == 1) or (lst[0][1] == 2) :
        warning()
        return
    if (x % 2 == 1) :
        bA2.config(image = red)
        bA2.image = red
        bA2.pack(ipady = 20, ipadx = 12)
        jouer_rouge("A2", x, b)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    else :
        bA2.config(image = blue)
        bA2.image = blue
        bA2.pack(ipady = 20, ipadx = 12)
        jouer_bleu("A2", x)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    if (x > 7) :
        draw()
        return
def place_A3() :
    global x
    global b
    global AI
    global k
    k = k + 1
    if (lst[0][0] == 1) or (lst[0][0] == 2) :
        warning()
        return
    if (x % 2 == 1) :
        bA3.config(image = red)
        bA3.image = red
        bA3.pack(ipady = 20, ipadx = 12)
        jouer_rouge("A3", x, b)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    else :
        bA3.config(image = blue)
        bA3.image = blue
        bA3.pack(ipady = 20, ipadx = 12)
        jouer_bleu("A3", x)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    if (x > 7) :
        draw()
        return
def place_B1() :
    global x
    global b
    global AI
    global k
    k = k + 1
    if (lst[1][2] == 1) or (lst[1][2] == 2) :
        warning()
        return
    if (x % 2 == 1) :
        bB1.config(image = red)
        bB1.image = red
        bB1.pack(ipady = 20, ipadx = 12)
        jouer_rouge("B1", x, b)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    else :
        bB1.config(image = blue)
        bB1.image = blue
        bB1.pack(ipady = 20, ipadx = 12)
        jouer_bleu("B1", x)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    if (x > 7) :
        draw()
        return
def place_B2() :
    global x
    global b
    global AI
    global k
    k = k + 1
    if (lst[1][1] == 1) or (lst[1][1] == 2) :
        warning()
        return
    if (x % 2 == 1) :
        bB2.config(image = red)
        bB2.image = red
        bB2.pack(ipady = 20, ipadx = 12)
        jouer_rouge("B2", x, b)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    else :
        bB2.config(image = blue)
        bB2.image = blue
        bB2.pack(ipady = 20, ipadx = 12)
        jouer_bleu("B2", x)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    if (x > 7) :
        draw()
        return
def place_B3() :
    global x
    global b
    global AI
    global k
    k = k + 1
    if (lst[1][0] == 1) or (lst[1][0] == 2) :
        warning()
        return
    if (x % 2 == 1) :
        bB3.config(image = red)
        bB3.image = red
        bB3.pack(ipady = 20, ipadx = 12)
        jouer_rouge("B3", x, b)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    else :
        bB3.config(image = blue)
        bB3.image = blue
        bB3.pack(ipady = 20, ipadx = 12)
        jouer_bleu("B3", x)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    if (x > 7) :
        draw()
        return
def place_C1() :
    global x
    global b
    global AI
    global k
    k = k + 1
    if (lst[2][2] == 1) or (lst[2][2] == 2) :
        warning()
        return
    if (x % 2 == 1) :
        bC1.config(image = red)
        bC1.image = red
        bC1.pack(ipady = 20, ipadx = 12)
        jouer_rouge("C1", x, b)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    else :
        bC1.config(image = blue)
        bC1.image = blue
        bC1.pack(ipady = 20, ipadx = 12)
        jouer_bleu("C1", x)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    if (x > 7) :
        draw()
        return
def place_C2() :
    global x
    global b
    global AI
    global k
    k = k + 1
    if (lst[2][1] == 1) or (lst[2][1] == 2) :
        warning()
        return
    if (x % 2 == 1) :
        bC2.config(image = red)
        bC2.image = red
        bC2.pack(ipady = 20, ipadx = 12)
        jouer_rouge("C2", x, b)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    else :
        bC2.config(image = blue)
        bC2.image = blue
        bC2.pack(ipady = 20, ipadx = 12)
        jouer_bleu("C2", x)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    if (x > 7) :
        draw()
        return
def place_C3() :
    global x
    global b
    global AI
    global k
    k = k + 1
    if (lst[2][0] == 1) or (lst[2][0] == 2) :
        warning()
        return
    if (x % 2 == 1) :
        bC3.config(image = red)
        bC3.image = red
        bC3.pack(ipady = 20, ipadx = 12)
        jouer_rouge("C3", x, b)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            print(k)
            play_AI()
    else :
        bC3.config(image = blue)
        bC3.image = blue
        bC3.pack(ipady = 20, ipadx = 12)
        jouer_bleu("C3", x)
        stop = win()
        if stop == 'R' :
            return
        x = x + 1
        if (k % 2 == 1) :
            play_AI()
    if (x > 7) :
        draw()
        return


def win() :
    wr0=wr1=wr2=wr3=wr4=wr5=wr6=wr7=wb0=wb1=wb2=wb3=wb4=wb5=wb6=wb7=0
    for i in range(0, 3) :
            if(lst[i][0]==1) :
                wr1 = wr1 + 1
            if(lst[i][1]==1) :
                print()
                wr2 = wr2 + 1
            if(lst[i][2]==1) :
                wr3 = wr3 + 1
            if(lst[i][0]==2) :
                wb1 = wb1 + 1
            if(lst[i][1]==2) :
                wb2 = wb2 + 1
            if(lst[i][2]==2) :
                wb3 = wb3 + 1
    for j in range(0, 3) :
            if(lst[0][j]==1) :
                wr4 = wr4 + 1
            if(lst[1][j]==1) :
                wr5 = wr5 + 1
            if(lst[2][j]==1) :
                wr6 = wr6 + 1
            if(lst[0][j]==2) :
                wb4 = wb4 + 1
            if(lst[1][j]==2) :
                wb5 = wb5 + 1
            if(lst[2][j]==2) :
                wb6 = wb6 + 1
    if(lst[0][0]==2)and(lst[1][1]==2)and(lst[2][2]==2) :
        wb7 = 3
    if(lst[0][2]==2)and(lst[1][1]==2)and(lst[2][0]==2) :
        wb0 = 3
    if(lst[0][0]==1)and(lst[1][1]==1)and(lst[2][2]==1) :
        wr7 = 3
    if(lst[0][2]==1)and(lst[1][1]==1)and(lst[2][0]==1) :
        wr0 = 3



    if(wr0==3)or(wr1==3)or(wr2==3)or(wr3==3)or(wr4==3)or(wr5==3)or(wr6==3)or(wr7==3) :
        w = 'R'
    elif(wb0==3)or(wb1==3)or(wb2==3)or(wb3==3)or(wb4==3)or(wb5==3)or(wb6==3)or(wb7==3) :
        w = 'B'
    else :
        w = 0
        
    if w=='B' :
        messagebox.showinfo('Victory', 'The Blue player as WON ! ')   
    if w=='R' :
        messagebox.showinfo('Victory', 'The Red player as WON ! ')
    return(w)

def warning() :
    messagebox.showerror("ERROR", "This case is already taken ! ")
    
def draw() :
    messagebox.showinfo("Draw", "It's a draw ! ")
    

def restart_game_blue() :
    global x
    global b
    global k
    global AI
    global CAS1
    global CAS2
    global CAS3
    global CAS4
    bC3.config(image = "")
    bC3.image = None
    bC3.pack(ipady = 70, ipadx = 70)
    bC2.config(image = "")
    bC2.image = None
    bC2.pack(ipady = 70, ipadx = 70)
    bC1.config(image = "")
    bC1.image = None
    bC1.pack(ipady = 70, ipadx = 70)
    bB3.config(image = "")
    bB3.image = None
    bB3.pack(ipady = 70, ipadx = 70)
    bB2.config(image = "")
    bB2.image = None
    bB2.pack(ipady = 70, ipadx = 70)
    bB1.config(image = "")
    bB1.image = None
    bB1.pack(ipady = 70, ipadx = 70)
    bA3.config(image = "")
    bA3.image = None
    bA3.pack(ipady = 70, ipadx = 70)
    bA2.config(image = "")
    bA2.image = None
    bA2.pack(ipady = 70, ipadx = 70)
    bA1.config(image = "")
    bA1.image = None
    bA1.pack(ipady = 70, ipadx = 70)
    for i in range(0, 3) :
        for j in range(0, 3) :
            lst[i][j] = 0
    b = 0
    x = 0
    AI = 0
    CAS1 = 0
    CAS2 = 0
    CAS3 = 0
    CAS4 = 0

    first_AI()
    return


def restart_game_red() :
    global x
    global b
    global k
    global AI
    global CAS1
    global CAS2
    global CAS3
    global CAS4
    bC3.config(image = "")
    bC3.image = None
    bC3.pack(ipady = 70, ipadx = 70)
    bC2.config(image = "")
    bC2.image = None
    bC2.pack(ipady = 70, ipadx = 70)
    bC1.config(image = "")
    bC1.image = None
    bC1.pack(ipady = 70, ipadx = 70)
    bB3.config(image = "")
    bB3.image = None
    bB3.pack(ipady = 70, ipadx = 70)
    bB2.config(image = "")
    bB2.image = None
    bB2.pack(ipady = 70, ipadx = 70)
    bB1.config(image = "")
    bB1.image = None
    bB1.pack(ipady = 70, ipadx = 70)
    bA3.config(image = "")
    bA3.image = None
    bA3.pack(ipady = 70, ipadx = 70)
    bA2.config(image = "")
    bA2.image = None
    bA2.pack(ipady = 70, ipadx = 70)
    bA1.config(image = "")
    bA1.image = None
    bA1.pack(ipady = 70, ipadx = 70)
    for i in range(0, 3) :
        for j in range(0, 3) :
            lst[i][j] = 0
    b = 2
    x = -1
    AI = 0
    CAS1 = 0
    CAS2 = 0
    CAS3 = 0
    CAS4 = 0
    return


def entry_red() :
    global first
    first = "red"
    insert.quit()
    insert.destroy()

def entry_blue() :
    global first
    first = "blue"
    insert.quit()
    insert.destroy()

def first_AI() :
    global k
    k = 1
    place_B2()
    return

def play_AI() :
    global AI
    global first
    global CAS1
    global CAS2
    global CAS3
    global CAS4
    AI = AI + 1
    wr0=wr1=wr2=wr3=wr4=wr5=wr6=wr7=wb0=wb1=wb2=wb3=wb4=wb5=wb6=wb7=0

###################### DEBUT DE PARTIE ############################

    if lst[1][1] == 0 :
        place_B2()
        return
    if (AI == 1) and (first == 'red') :
        foo = ['a', 'b', 'c', 'd']
        apply = random.choice(foo)
        if apply == 'a' :
            place_A1()
            return
        if apply == 'b' :
            place_A3()
            return
        if apply == 'c' :
            place_C3()
            return
        if apply == 'd' :
            place_C1()
            return
    if (AI == 1) and (first == 'blue') :
        foo = ['a', 'b']
        apply = random.choice(foo)
        if lst[0][2] == 1 :
            if apply == 'a' :
                place_A3()
                return
            if apply == 'b' :
                place_C3()
                return
        if lst[0][1] == 1 :
            if apply == 'a' :
                CAS1 = 1
                place_B1()
                return
            if apply == 'b' :
                CAS2 = 1
                place_B3()
                return
        if lst[0][0] == 1 :
            if apply == 'a' :
                place_A1()
                return
            if apply == 'b' :
                place_C3()
                return
        if lst[1][0] == 1 :
            if apply == 'a' :
                CAS3 = 1
                place_A2()
                return
            if apply == 'b' :
                CAS1 = 1
                place_C2()
                return
        if lst[2][0] == 1 :
            if apply == 'a' :
                place_C1()
                return
            if apply == 'b' :
                place_A3()
                return
        if lst[2][1] == 1 :
            if apply == 'a' :
                CAS3 = 1
                place_B1()
                return
            if apply == 'b' :
                CAS4 = 1
                place_B3()
                return
        if lst[2][2] == 1 :
            if apply == 'a' :
                place_A1()
                return
            if apply == 'b' :
                place_C3()
                return
        if lst[1][2] == 1 :
            if apply == 'a' :
                CAS4 = 1
                place_A2()
                return
            if apply == 'b' :
                CAS2 = 1
                place_C2()
                return
###################### VICTOIRE BLEU ##############################
    for i in range(0, 3) :
        if(lst[i][0]==2) :
            wb1 = wb1 + 1
            if(wb1 == 2) and (lst[0][0] != 1) and (lst[1][0] != 1) and (lst[2][0] != 1) :
                if lst[0][0] == 0 :
                    place_A3()
                    return
                if lst[1][0] == 0 :
                    place_B3()
                    return
                if lst[2][0] == 0 :
                    place_C3()
                    return
        if(lst[i][1]==2) :
            wb2 = wb2 + 1
            if(wb2 == 2) and (lst[0][1] != 1) and (lst[1][1] != 1) and (lst[2][1] != 1) :
                if lst[0][1] == 0 :
                    place_A2()
                    return
                if lst[1][1] == 0 :
                    place_B2()
                    return
                if lst[2][1] == 0 :
                    place_C2()
                    return
        if(lst[i][2]==2) :
            wb3 = wb3 + 1
            if(wb3 == 2) and (lst[0][2] != 1) and (lst[1][2] != 1) and (lst[2][2] != 1) :
                if lst[0][2] == 0 :
                    place_A1()
                    return
                if lst[1][2] == 0 :
                    place_B1()
                    return
                if lst[2][2] == 0 :
                    place_C1()
                    return
        if(lst[i][i]==2) :
            wb7 = wb7 + 1
            if(wb7 == 2) and (lst[0][0] != 1) and (lst[1][1] != 1) and (lst[2][2] != 1) :
                if lst[0][0] == 0 :
                    place_A3()
                    return
                if lst[1][1] == 0 :
                    place_B2()
                    return
                if lst[2][2] == 0 :     
                    place_C1()
                    return
    for j in range(0, 3) :
        if(lst[0][j]==2) :
            wb4 = wb4 + 1
            if(wb4 == 2) and (lst[0][0] != 1) and (lst[0][1] != 1) and (lst[0][2] != 1) :
                if lst[0][0] == 0 :
                    place_A3()
                    return
                if lst[0][1] == 0 :
                    place_A2()
                    return
                if lst[0][2] == 0 :
                    place_A1()
                    return
        if(lst[1][j]==2) :
            wb5 = wb5 + 1
            if(wb5 == 2) and (lst[1][0] != 1) and (lst[1][1] != 1) and (lst[1][2] != 1) :
                if lst[1][0] == 0 :
                    place_B3()
                    return
                if lst[1][1] == 0 :
                    place_B2()
                    return
                if lst[1][2] == 0 :
                    place_B1()
                    return
        if(lst[2][j]==2) :
            wb6 = wb6 + 1
            if(wb6 == 2) and (lst[2][0] != 1) and (lst[2][1] != 1) and (lst[2][2] != 1) :
                if lst[2][0] == 0 :
                    place_C3()
                    return
                if lst[2][1] == 0 :
                    place_C2()
                    return
                if lst[2][2] == 0 :
                    place_C1()
                    return
        if ((lst[0][2] == 2)and(lst[1][1] == 2)) or ((lst[0][2] == 2)and(lst[2][0] == 2)) or ((lst[2][0] == 2)and(lst[1][1] == 2)) :
            if lst[0][2] == 0 :
                place_A1()
                return
            if lst[1][1] == 0 :
                place_B2()
                return
            if lst[2][0] == 0 :
                place_C3()
                return
        

###################### VICTOIRE ROUGE ##############################
    for i in range(0, 3) :
        if(lst[i][0]==1) :
            wr1 = wr1 + 1
            if(wr1 == 2) and (lst[0][0] != 2) and (lst[1][0] != 2) and (lst[2][0] != 2) :
                if lst[0][0] == 0 :
                    place_A3()
                    return
                if lst[1][0] == 0 :
                    place_B3()
                    return
                if lst[2][0] == 0 :
                    place_C3()
                    return
        if(lst[i][1]==1) :
            wr2 = wr2 + 1
            if(wr2 == 2) and (lst[0][1] != 2) and (lst[1][1] != 2) and (lst[2][1] != 2) :
                if lst[0][1] == 0 :
                    place_A2()
                    return
                if lst[1][1] == 0 :
                    place_B2()
                    return
                if lst[2][1] == 0 :
                    place_C2()
                    return
        if(lst[i][2]==1) :
            wr3 = wr3 + 1
            if(wr3 == 2) and (lst[0][2] != 2) and (lst[1][2] != 2) and (lst[2][2] != 2) :
                if lst[0][2] == 0 :
                    place_A1()
                    return
                if lst[1][2] == 0 :
                    place_B1()
                    return
                if lst[2][2] == 0 :
                    place_C1()
                    return
        if(lst[i][i]==1) :
            wr7 = wr7 + 1
            if(wr7 == 2) and (lst[0][0] != 2) and (lst[1][1] != 2) and (lst[2][2] != 2) :
                if lst[0][0] == 0 :
                    place_A3()
                    return
                if lst[1][1] == 0 :
                    place_B2()
                    return
                if lst[2][2] == 0 :     
                    place_C1()
                    return
    for j in range(0, 3) :
        if(lst[0][j]==1) :
            wr4 = wr4 + 1
            if(wr4 == 2) and (lst[0][0] != 2) and (lst[0][1] != 2) and (lst[0][2] != 2) :
                if lst[0][0] == 0 :
                    place_A3()
                    return
                if lst[0][1] == 0 :
                    place_A2()
                    return
                if lst[0][2] == 0 :
                    place_A1()
                    return
        if(lst[1][j]==1) :
            wr5 = wr5 + 1
            if(wr5 == 2) and (lst[1][0] != 2) and (lst[1][1] != 2) and (lst[1][2] != 2) :
                if lst[1][0] == 0 :
                    place_B3()
                    return
                if lst[1][1] == 0 :
                    place_B2()
                    return
                if lst[1][2] == 0 :
                    place_B1()
                    return
        if(lst[2][j]==1) :
            wr6 = wr6 + 1
            if(wr6 == 2) and (lst[2][0] != 2) and (lst[2][1] != 2) and (lst[2][2] != 2) :
                if lst[2][0] == 0 :
                    place_C3()
                    return
                if lst[2][1] == 0 :
                    place_C2()
                    return
                if lst[2][2] == 0 :
                    place_C1()
                    return
        if ((lst[0][2] == 1)and(lst[1][1] == 1)) or ((lst[0][2] == 1)and(lst[2][0] == 1)) or ((lst[2][0] == 1)and(lst[1][1] == 1)) :
            if lst[0][2] == 0 :
                place_A1()
                return
            if lst[1][1] == 0 :
                place_B2()
                return
            if lst[2][0] == 0 :
                place_C3()
                return

################## CAS APRES VERIFICATION #######################

    if (first == 'red') and (AI == 2) :
        if lst[0][2] == 0 :
            place_A1()
            return
        if lst[0][0] == 0 :
            place_A3()
            return
        if lst[2][2] == 0 :
            place_C1()
            return
        if lst[2][0] == 0 :
            place_C3()
            return
    if (AI == 2) and (first == 'blue') :
        if CAS1 == 1 :
            place_C1()
            return
        if CAS2 == 1 :
            place_C3()
            return
        if CAS3 == 1 :
            place_A1()
            return
        if CAS4 == 1 :
            place_A3()
            return

################# CAS DE DERNIER RECOURS #########################
    if lst[1][1] == 0 :
        place_B2()
        return
    if lst[0][2] == 0 :
        place_A1()
        return
    if lst[0][1] == 0 :
        place_A2()
        return
    if lst[0][0] == 0 :
        place_A3()
        return
    if lst[1][2] == 0 :
        place_B1()
        return
    if lst[1][0] == 0 :
        place_B3()
        return
    if lst[2][2] == 0 :
        place_C1()
        return
    if lst[2][1] == 0 :
        place_C2()
        return
    if lst[2][0] == 0 :
        place_C3()
        return
    
        
from uarm.wrapper import SwiftAPI
swift = SwiftAPI()
swift.set_speed_factor(3)
swift.waiting_ready()
root = tk.Tk()
insert = tk.Tk()

text = tk.Label(insert, text="choose the color of the beginner then close the window")
text.pack()
bb1 = tk.Button(insert, text='blue', command=entry_blue, width = 25)
bb1.pack(side = tk.BOTTOM)
r1 = tk.Button(insert, text='red', command=entry_red, width = 25)
r1.pack(side = tk.BOTTOM)

insert.mainloop()

#define menu options
menu = tk.Menu(root)
game_menu = tk.Menu(menu)
root.config(menu=menu)
new_menu = tk.Menu(game_menu)
new_menu.add_command(label="Blue", command=restart_game_blue)
new_menu.add_command(label="Red", command=restart_game_red)


game_menu.add_cascade(label="New Game", menu=new_menu)
game_menu.add_command(label="Exit", command=root.destroy)

menu.add_cascade(label="Game", menu=game_menu)

b = 0
x = 0
k = 0


if first == 'blue' :

    x = 0
    b = 0
    AI = 0

    frame = tk.Frame(root)
    frame.pack()
    framebot = tk.Frame(root)
    framebot.pack(side = tk.BOTTOM)
    frametop = tk.Frame(root)
    frametop.pack(side = tk.TOP)

    red = ImageTk.PhotoImage(file="red.png")
    blue = ImageTk.PhotoImage(file="blue.png")

    bA1 = tk.Button(frame, command=place_A1)
    bA1.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bA2 = tk.Button(frame, command=place_A2)
    bA2.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bA3 = tk.Button(frame, command=place_A3)
    bA3.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bC1 = tk.Button(framebot, command=place_C1)
    bC1.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bC2 = tk.Button(framebot, command=place_C2)
    bC2.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bC3 = tk.Button(framebot, command=place_C3)
    bC3.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bB1 = tk.Button(frametop, command=place_B1)
    bB1.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bB2 = tk.Button(frametop, command=place_B2)
    bB2.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bB3 = tk.Button(frametop, command=place_B3)
    bB3.pack(ipady = 70, ipadx = 70, side=tk.LEFT)

    first_AI()

else :
    x = -1
    b = 2
    AI = 0

    frame = tk.Frame(root)
    frame.pack()
    framebot = tk.Frame(root)
    framebot.pack(side = tk.BOTTOM)
    frametop = tk.Frame(root)
    frametop.pack(side = tk.TOP)

    red = ImageTk.PhotoImage(file="red.png")
    blue = ImageTk.PhotoImage(file="blue.png")

    bA1 = tk.Button(frame, command=place_A1)
    bA1.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bA2 = tk.Button(frame, command=place_A2)
    bA2.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bA3 = tk.Button(frame, command=place_A3)
    bA3.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bC1 = tk.Button(framebot, command=place_C1)
    bC1.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bC2 = tk.Button(framebot, command=place_C2)
    bC2.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bC3 = tk.Button(framebot, command=place_C3)
    bC3.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bB1 = tk.Button(frametop, command=place_B1)
    bB1.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bB2 = tk.Button(frametop, command=place_B2)
    bB2.pack(ipady = 70, ipadx = 70, side=tk.LEFT)
    bB3 = tk.Button(frametop, command=place_B3)
    bB3.pack(ipady = 70, ipadx = 70, side=tk.LEFT)

root.mainloop()

