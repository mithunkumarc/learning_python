#### remembers order
### output is same for dict and OrderedDict, need more example


            
            d = {}
            d['a'] = 1
            d['b'] = 2
            d['c'] = 3
            d['d'] = 4

            for key, value in d.items():
                print(key, value)

            print('*'*50)

            from collections import OrderedDict
            d = OrderedDict()
            d['a'] = 1
            d['b'] = 2
            d['c'] = 3
            d['d'] = 4

            for key, value in d.items():
                print(key, value)
