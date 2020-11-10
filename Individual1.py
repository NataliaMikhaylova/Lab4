#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Вывести «столбиком» его первый, второй, пятый, шестой, девятый,
# десятый и т. д. символы.

if __name__ == '__main__':
    word = input("Введите предложение: ")
    i = 0
    while i <= len(word):
        print(word[i])
        if i + 1 < len(word):
            print(word[i+1])
        i += 4
