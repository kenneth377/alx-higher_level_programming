#!/usr/bin/python3


def no_c(str):
    newstr = ""
    for i in str:
        if i != "c" and  i != "C":
            newstr += i
    return newstr
