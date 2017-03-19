#!/usr/bin/env python

class Anagram():
    def __init__(self):
        pass
        
    @classmethod
    def get_list(self):
        l = []
        length = raw_input('Enter length of list: ')
        for item in range(int(length)):
            l.append(raw_input('Enter element #{}: '.format(item)))
        return l

    @classmethod
    def compare(self,x,y):
        temp_y = y
        for c in x:
            temp_y = temp_y.replace(c,'',1)
        if len(temp_y) == 0:
            print '{} is anagram with {}'.format(x,y)

    def check_for_anagram(self,l):
        for i,e1 in enumerate(l):
            for e2 in l[i+1:]:
                if len(e1) == len(e2):
                    self.compare(e1,e2)

if __name__ == "__main__":
    a = Anagram()
    a.check_for_anagram(a.get_list())