#!/usr/bin/python3

def add_tuple(a, b):
    newt = ()
    lena = 2 -len(a)
    lenb = 2 -len(b)
    if len(a)<2:
        ze = 0,
        a = (a+ ze*lena)
    if len(b)<2:
        ze = 0,
        b = (b + ze*lenb)
    else:
        a = a[:2]
        b = b[:2]

    for i in range(2):
        newv = a[i]+b[i]
        newt =newt+(newv, )

    return newt
