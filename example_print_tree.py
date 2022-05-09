#!/usr/bin/python3
#-*- coding: utf-8 -*-

class Wezel:
    potomkowie = None
    atrybut = None
    wartosc = None
    klasa = None

def wyswietlDrzewo(drzewo,przesuniecie):
    if drzewo.atrybut!=None:
        print(" "*przesuniecie,end="")
        if drzewo.wartosc: print(drzewo.wartosc,end=" -> ")
        print("Atrybut",drzewo.atrybut)
        for p in drzewo.potomkowie:
            wyswietlDrzewo(p,przesuniecie+4)
    else:
        print(" "*przesuniecie,end="")
        print(drzewo.wartosc, "->" ,drzewo.klasa)

def buduj(test):
    w = Wezel()
    w.potomkowie = []
    klucz, element = test.popitem()
    w.atrybut = klucz
    for t in element:
        if isinstance(element[t], (dict)):
            nowyWezel=buduj(element[t])
            nowyWezel.wartosc = t
            w.potomkowie.append(nowyWezel)
        else:
            nowyWezel = Wezel()
            nowyWezel.wartosc = t
            nowyWezel.klasa = element[t]
            w.potomkowie.append(nowyWezel)
    return w

test = {1:{"n":"tak", "m":{2:{"a":"nie", "b":"tak"}}, "o":"nie"}} #testowe dane
# test = {1: {'old': 'down', 'mid': {2: {'yes': 'down', 'no': 'up'}}, 'new': 'up'}}

w = buduj(test)
wyswietlDrzewo(w,0)