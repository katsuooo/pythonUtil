''' dict sort '''

x = [3,2,1]
x.sort()
print(x)
x = [3,2,1]
y = sorted(x)
print(y)
'''
sort() is substituted original array
'''
from operator import itemgetter, attrgetter
d = [{'num':'3'},{'num':'2'},{'num':'1'}]
y = sorted(d, key=itemgetter('num'))
print(y) #[{'num': '1'}, {'num': '2'}, {'num': '3'}]
d.sort(key=itemgetter('num'))
print(d)
dnum = [{'num': 3},{'num':2},{'num':1}]
dnum.sort(key=itemgetter('num'))
print(dnum)