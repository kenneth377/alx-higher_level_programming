#!/usr/bin/python3


def new_in_list(li, idx, new_element):
    newl = li[:]
    if 0< idx < len(li):
        newl[idx] = new_element
        return newl
    return li
