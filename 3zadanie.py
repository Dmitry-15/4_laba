#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = 10
    b = 5
    c = 0.5

    for a in range(1, 10):
        for b in range(1, 20):
            for c in range(1, 200):
                if (10 * a + 5 * b + 0.5 * c == 100) and (a + b + c == 100):
                    print(f"Быков - {a}, коров - {b}, телят - {c}")
