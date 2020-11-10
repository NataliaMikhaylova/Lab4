#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Удалить из него все буквы с (как в кириллице так и на латинице).

if __name__ == '__main__':
    word = input("Введите предложение: ")
    s = len(word)
    for i in range(s):
        if word[i] == "c" or word[i] == 'с':
            word = word.replace(word[i], ' ')
    print(word)
