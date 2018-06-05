#!/usr/bin/python3
# -*- coding: utf-8 -*-

def exo01():
    print("mon text"*500)

def exo02():
    i = 1
    while i != 1000:
        print(i)
        i = i +2

def exo03():
    i = 0
    j = 13
    while i>=0 and i<=10:
        print(i*j)
        i = i+1

def exo04():
    mot = input("entrer un mot")
    print(len(mot))

def exo05():
    print("Entrer un nombre")
    nbr=int(input())
    if (nbr % 2 == 1):
        print("impair")
    else:
        print("pair")

def exo06():
    print("entrer un nombre compris entre 10 et 20")
    nbr=int(input())
    if(nbr >= 10 and nbr <= 20):
        print(nbr)
    else:
        exo06()


def exo7(entier):
    i=1
    while i<=10:
        print(entier + i)
        i += 1

# exo7(int(input()))

def exo8 ():
    print("saisir un chiffre")
    nbr = int(input())
    i = 0
    j = nbr
    while i >= 0 and i <= 10:
        print(i * j)
        i = i + 1

def exo9():
    val = int(input("entrez un nombre :"))
    somme = 0
    for i in range(0 , val+1):
        somme = i + somme
    print(somme)

def exo10():
    age = int (input ("Entrez son âge:"))
    if age == 6 or age == 7:
        print ("Poussin de 6 à 7 ans")
    elif age == 8 or age == 9:
        print("Pupille de 8 à 9 ans")
    elif age == 10 or age == 11:
        print("Mimmie de 10 à 11 ans")
    elif age >= 12:
        print("Cadet apres 12 ans")


def exo11():
    pU = int(input("Prix unitaire"))
    nBr = int(input("Nombre d'article"))

    totalHt = pU*nBr
    totalTtc = totalHt*1.20
    print(totalHt)
    print(totalTtc)


def exo12():
    nbr = int(input("donner un nombre "))
    fact = 1
    i = 1
    while i <= nbr:
        fact = fact*i
        i = i + 1
    print(" factoriel de " + str(nbr) + " = " + str(fact))

def exo13():
    nombre = int(input("donner un nombre entier "))
    binaire = []
    while nombre :
        reste = nombre % 2
        nombre = nombre//2
        binaire.append(reste)
    print(binaire)


def exo14():
    somme = 0
    for i in range(1,1000):
        if i % 3 == 0 and i % 5 == 0:
            somme = i + somme
    print(somme)

def exo15():
    a = 0
    b = 1
    c = 0

    nombre = int(input("entrer nombre"))
    for x in range(0, nombre):
        print(a, b)
        c = a + b
        a = b
        b = c

    #print(a, b)

def exo16():
    val = 0
    count = []
    while True:
        val = val + 1
        for i in range(1, 10):
            if val%i == 0:
                count.append(1)
        if len(count) >= 9:
            print(val)
            break
        print(len(count))
        count = []

import random, emoji

def exo17():
    life = 9
    rand = random.randint(1, 100)
    while life >= 0:
        life = life - 1
        valeur = int(input("entre un nombre: "))
        if valeur > rand:
            print("plus petit")
        elif valeur < rand:
            print("plus grand")
        else:
            print(emoji.emojize("WIN :thumbs_up:", use_aliases=True))
            break
        print(emoji.emojize(":heart:"*life, use_aliases=True))
    if life == 0:
        print("Game Over")

exo16()


