#!/usr/bin/env python
length = raw_input('Enter length of list: ')

l = []
for item in range(int(length)):
    l.append(raw_input('Enter element #{}: '.format(item)))

def compare(x,y):
    temp_y = y
    for c in x:
        temp_y = temp_y.replace(c,'')
    if len(temp_y) == 0:
        print '{} is anagram with {}'.format(x,y)

for i,e1 in enumerate(l):
    for e2 in l[i+1:]:
        if len(e1) == len(e2):
            compare(e1,e2)