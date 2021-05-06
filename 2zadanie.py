#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input("Введите первое число: "))
    b = int(input("Введите второк число: "))
    c = int(input("Введите третье число: "))

    if b % 2 == 0 or a % 2 == 0:
        print("YES")
    elif c % 2 == 0 or a % 2 == 0:
        print("YES")
    elif c % 2 == 0 or b % 2 == 0:
        print("YES")
    else:
        print("NO")
