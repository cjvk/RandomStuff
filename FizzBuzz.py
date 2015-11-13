#!/usr/bin/python

import sys

MAX=21

def printWithNewlines():
    for i in range(1, MAX):
        modthree = i % 3
        modfive = i % 5
        if modthree == 0 and modfive == 0:
            print 'FizzBuzz'
        elif modthree == 0:
            print 'Fizz'
        elif modfive == 0:
            print 'Buzz'
        else:
            print i

def printWithoutNewlinesWithSpaces():
    for i in range(1, MAX):
        modthree = i % 3
        modfive = i % 5
        if modthree == 0:
            print 'Fizz',
        if modfive == 0:
            print 'Buzz',
        if modthree != 0 and modfive != 0:
            print i,

def printWithoutNewlinesWithoutSpaces():
    for i in range(1, MAX):
        modthree = i % 3
        modfive = i % 5
        if modthree == 0:
            sys.stdout.write('Fizz')
        if modfive == 0:
            sys.stdout.write('Buzz')
        if modthree != 0 and modfive != 0:
            sys.stdout.write(str(i))
    print

# printWithNewlines()
# printWithoutNewlinesWithSpaces()
printWithoutNewlinesWithoutSpaces()
