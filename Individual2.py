#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово. Проверить, является ли оно палиндромом.

if __name__ == '__main__':
    word = input("Введите слово: ")
    rev = ''.join(reversed(word))

    if word == rev:
        print("Слово является палиндромом! ")
    else:
        print("Слово не является палиндромом( ")
