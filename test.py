#!/usr/bin/env python
# coding=utf-8
__autor__='cheng'

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
        self.start=0
        self.max=len(arg)
    def __iter__(self):
        print('run iter...')
        return self
    def __next__(self):
        print('run next...',end='')
        if self.start >= self.max:
            print('StopIteration is ...')
            raise StopIteration
        result=self.arg[self.start]
        self.start +=1
        return result
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
        return 0

if __name__ == '__main__':
    l=[1,3,4,5,6,5]
    tfl=Testforoverload(l)
    for x in tfl:
        print(x)
    print(oct(tfl))
    print(1 in tfl)
    print(tfl[1])
