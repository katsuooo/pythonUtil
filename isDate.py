'''date exsists check in string'''
'''return val true,false ????
sep type ? /, . , none
'''


import datetime

class isDate:
    '''check isDate in text
    return {'judge': True or False, 'type': if judge==True type == separator type ./-none}
    '''
    def __init__(self):
        pass
    def checkSepSlash(self, text):
        '''yyyy/mm/dd check'''
        try:
            testdate = datetime.datetime.strptime(text, '%Y/%m/%d')
            print(testdate)
            judge = {'judge': True, 'type': 'SEP_/'}
        except ValueError:
            judge = {'judge': False}
        return judge
    def checkSepDot(self, text):
        '''yyyy.mm.dd check'''
        try:
            testdate = datetime.datetime.strptime(text, '%Y.%m.%d')
            print(testdate)
            judge = {'judge': True, 'type': 'SEP_.'}
        except ValueError:
            judge = {'judge': False}
        return judge
    def checkSepNone(self, text):
        '''yyyymmdd check'''
        try:
            testdate = datetime.datetime.strptime(text, '%Y%m%d')
            print(testdate)
            judge = {'judge': True, 'type': 'SEP_NONE'}
        except ValueError:
            judge = {'judge': False}
        return judge
    def checkSepHihun(self, text):
        '''yyyy-mm-dd check'''
        try:
            testdate = datetime.datetime.strptime(text, '%Y-%m-%d')
            print(testdate)
            judge = {'judge': True, 'type': 'SEP_-'}
        except ValueError:
            judge = {'judge': False}
        return judge
    def check(self, text):
        judge = self.checkSepSlash(text)
        if judge['judge'] == True:
            return judge
        judge = self.checkSepDot(text)        
        if judge['judge'] == True:
            return judge
        judge = self.checkSepNone(text)        
        if judge['judge'] == True:
            return judge
        judge = self.checkSepHihun(text)        
        if judge['judge'] == True:
            return judge
        return judge

if __name__ == '__main__':
    text1 = '2019/05/12'
    print('//test text1 - ', text1)
    id = isDate()
    print(id.check(text1))
    text2 = '2019.05.12'
    print('//test text2 - ', text2)
    print(id.check(text2))
    text3 = '2019-05-12'    
    print('//test text3 - ', text3)
    print(id.check(text3))
    text4 = '20190512'    
    print('//test text4 - ', text4)
    print(id.check(text4))