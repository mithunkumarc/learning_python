#### dict-like class for creating a single view of multiple mappings
#### simlar to dictionary , but consists of multiple dictionary

        from collections import ChainMap
        a = {'a':'A','b':'B'}
        b = {'c':'C','d':'D'}
        c = {'1':'one'}
        cm = ChainMap(a,b,c)
        print(cm)
        print(cm['a']) # A
        print(cm['b']) # B
        print(cm['1']) # one
