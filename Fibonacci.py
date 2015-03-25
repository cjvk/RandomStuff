#!/usr/bin/python

def nextFibPair(theTuple):
    return (theTuple[1], theTuple[0]+theTuple[1])

def goodEnuf(lowerRatio, higherRatio):
    return higherRatio - lowerRatio <= 0.00000000001

def ratio(theTuple):
    return float(theTuple[0])/float(theTuple[1])

FIRST_TUPLE=(1, 1)
MAXIMUM_ITERATIONS=100

x = FIRST_TUPLE
ratios = [ratio(FIRST_TUPLE), None]
setUpperRatio = False

for i in range(0, MAXIMUM_ITERATIONS):
    x = nextFibPair(x)
    newratio = ratio(x)
    if setUpperRatio:
        ratios[0] = newratio
    else:
        ratios[1] = newratio
    setUpperRatio = not setUpperRatio
    if goodEnuf(ratios[1], ratios[0]):
        break

error = (ratios[0]-ratios[1])/2
bestguess = ratios[0]-error
print 'The golden ratio is %s with an error of %s, after %i iterations' % (str(bestguess), str(error), i)
