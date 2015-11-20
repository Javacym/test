#!/usr/bin/env python
# coding=utf-8

import os

pkgs='''
apm install vim-mode
apm install ex-mode
apm install atom-terminal
apm install vim-mode-plus
apm install script
'''

pkgs=[i for i in pkgs.split('\n') if i]

def main():
    for pkg in pkgs:
        print('Installing package-->'+pkg)
        f=os.popen(pkg).read()
        if f[:10] != 'Installing':
            print(f)
    print('\nfinished!')

def search(keyword):
    s='apm --color=False search '+keyword
    f=os.popen(s).read()
    print('>>>>',f)

if __name__=='__main__':
    # main()
    search('vim')
