#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    x1 = int(input("x1= "))
    x2 = int(input("x2= "))
    p = 8 * x1 + 2 * x2

    if 200 < p < 500:
        p = p / 100 * 97
        print(p)
    elif 500 < p < 800:
        p = p / 100 * 95
        print(p)
    elif 800 < p < 1000:
        p = p / 100 * 93
        print(p)
    elif p > 1000:
        p = p / 100 * 91
        print(p)
    else:
        print("Скидки нет!")
