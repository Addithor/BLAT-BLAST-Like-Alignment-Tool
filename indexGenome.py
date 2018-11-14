import sys, collections, math, random
import numpy as np

def createIndex(string, k):
    # Create a dictionary that will hold indexes
    r = collections.defaultdict()

    # Roll through the string and add indexes for all non-overlaping k-meres
    for i in range(0, len(string) - k + 1, k):
        if r.get(string[i: i+k]):
            r[string[i: i+k]].append(i)
            print(i)
        else:
            print(i)
            r[string[i: i+k]] = [i]
    
    return r


"""
string = 'AAATTTCCCGGGAAA'
k = 3

index = collections.defaultdict()

index = createIndex(string, k)

for key, value in sorted(index.items()):
	print(key, '-> ', end = '')
	value = sorted(value)
	for j in range(len(value)):
		if j > 0:
			print(', ', sep='', end = '')
		print(value[j], end = '')
	print('')
    """