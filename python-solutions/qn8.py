#!/usr/bin/env python3

def valid_nep_name(name):
    name = name.strip()
    spaces = 0
    for c in name:
        if c == ' ':
            spaces += 1
    if spaces == 0:
        return -1
    return spaces + 1

def main():
    print(valid_nep_name("Ramesh Poudel"))
    print(valid_nep_name("RameshPoudel"))
    print(valid_nep_name("Ramesh Poudel  "))
    print(valid_nep_name(" Ramesh Poudel Prasad"))

main()
