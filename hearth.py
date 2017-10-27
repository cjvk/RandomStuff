#!/usr/bin/python

import random

ALPHABET_26 = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
ALPHABET_15 = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    #'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    #'U', 'V', 'W', 'X', 'Y', 'Z'
]
ALPHABET_10 = ['A', 'E', 'H', 'R', 'T', 'K', 'L', 'M', 'N', 'O']
ALPHABET_5 = ['A', 'E', 'H', 'R', 'T']

ALPHABET = ALPHABET_5

def randomChar():
    return random.choice(ALPHABET)

#MAXIMUM = 20000000
MAXIMUM = 10000000

def nextLetter(l):
    l.insert(len(l), randomChar())
    l.pop(0)

def isHeart(l):
    return l == ['H', 'E', 'A', 'R', 'T']

def isEarth(l):
    return l == ['E', 'A', 'R', 'T', 'H']

def runOnce():
    # initialize
    heart_index = None
    earth_index = None
    l = [randomChar(), randomChar(), randomChar(), randomChar(), randomChar()]
    index = 0

    # not the case that both are set
    # either one is not set
    # one or the other is not set
    while index < MAXIMUM and (heart_index == None or earth_index == None):
        if earth_index == None and isEarth(l):
            earth_index = index
        if heart_index == None and isHeart(l):
            heart_index = index
        nextLetter(l)
        index = index + 1

    return (heart_index, earth_index)

def runN(n):
    # heart_total, earth_total, trials
    stats = [0, 0, 0]
    for i in range(n):
        t = runOnce()
        stats[0] = stats[0] + t[0]
        stats[1] = stats[1] + t[1]
        stats[2] = stats[2] + 1
    heart_average = (stats[0] * 1.0) / stats[2]
    earth_average = (stats[1] * 1.0) / stats[2]
    print('totals after ' + str(stats[2]) + ' runs')
    print('heart average: ' + str(heart_average))
    print('earth average: ' + str(earth_average))

def run():

    # initialize
    heart_index = None
    earth_index = None
    l = [randomChar(), randomChar(), randomChar(), randomChar(), randomChar()]
    index = 0

    # not the case that both are set
    # either one is not set
    # one or the other is not set
    while index < MAXIMUM and (heart_index == None or earth_index == None):
        if (index % 1000000) == 0:
            print(l)
        if earth_index == None and isEarth(l):
            earth_index = str(index)
            print('found earth index! (' + earth_index + ')')
        if heart_index == None and isHeart(l):
            heart_index = str(index)
            print('found heart index! (' + heart_index + ')')
        nextLetter(l)
        index = index + 1

    print('heart_index=' + (heart_index or 'nope'))
    print('earth_index=' + (earth_index or 'nope'))
    

runN(10000)
