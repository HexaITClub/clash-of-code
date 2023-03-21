#!/usr/bin/env python3

def valid_nep_name(name):
    name = name.strip()
    name_arr = name.split(" ")
    if len(name_arr) == 1: return -1

    spaces = 0
    for c in name_arr:
        if c == ' ' or c == '':
            continue
        else:
            spaces += 1
    if spaces == 0:
        return -1
    return spaces

def main():
    print(valid_nep_name("Ramesh   Poudel"))
    print(valid_nep_name("RameshPoudel"))
    print(valid_nep_name("Ramesh Poudel  "))
    print(valid_nep_name(" Ramesh Poudel Prasad"))

main()
