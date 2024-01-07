#!/usr/bin/python3

def replace_in_list(li, idx, new_element):
    if 0 < idx < len(li):
        li[idx] = new_element
    return li
