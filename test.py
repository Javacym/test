#!/usr/bin/env python
# coding=utf-8

'''test a overload class
    test:
    __init__
    __iter__ __next__
    __getitem__ __setitem__
    __index__
    __contains__
    '''
class Testforoverload(object):
    """docstring for Testforoverload"""
    def __init__(self, arg):
        print('init...')
        super(Testforoverload, self).__init__()
        self.arg = arg
        self.start=-1
        self.max=len(arg)
    def __iter__(self):
        print('run iter...')
        return self
    def __next__(self):
        print('run next...')
        if self.start > self.max:
            raise StopIteration
        self.start +=1
        return self.arg[start]
    def __getitem__(self,index):
        print('run getitem...')
        return self.arg[index]
    def __setitem__(self,index,value):
        print('run setitem...')
        self.arg[index] = value
    def __contains__(self,item):
        print('run contains')
        return item in self.arg
    def __index__(self):
        print('run index...')
        return self.arg.__index__()

if __name__ == '__main__':
    l=[1,3,4,5,6,5]

    tfl=Testforoverload(l)
    print(tfl[1])
