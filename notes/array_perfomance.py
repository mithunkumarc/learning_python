'''
    comparing array performance with list
'''

import timeit


code = '''
import array
a = array.array("i",[])
for i in range(1,10000):
    a.append(i)
'''
print('time took by array',timeit.timeit(stmt=code,number=100))


code = '''
l = []
for i in range(1,10000):
    l.append(i)
'''
print('time took by list',timeit.timeit(stmt=code,number=100))