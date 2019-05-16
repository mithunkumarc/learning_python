#### dict subclass that calls a factory function to supply missing values


        from collections import defaultdict
        # defaultdict(callable) : callable :function
        icecreams = defaultdict(lambda : 25)
        icecreams['vanilla'] = 30
        icecreams['chcolate'] = 40
        icecreams['pista']
        print(icecreams) # pista will get default value 25

        #defaultdict(<function <lambda> at 0x7f92e5ee1e18>, 
        # {'vanilla': 30, 'chcolate': 40, 'pista': 25})
