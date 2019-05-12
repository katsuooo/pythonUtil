''' os detect '''
'''win 10 check >>> check other os!
'''

import os
import platform
class detOs:
    def __init__(self):
        print('os.name : ', os.name)
        print('platform.system : ', platform.system())
        print('platform.release : ', platform.release())

if __name__ == '__main__':
    detOs()

''' win10 
D:\choParser\pgView\testChromeOn>python
os.name :  nt
platform.system :  Windows
platform.release :  10
'''
