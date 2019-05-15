#### Counter : dict subclass for counting hashable objects
#### similar to dict , but values are their counts(number of times they appear)
#### count value can be set like dict values

        from collections import Counter

        c = Counter(['one',123,True,True,False])
        print(c.keys()) # dict_keys(['one', 123, True, False])
        print(c.values()) # dict_values([1, 1, 2, 1])

        # new count value for python and java
        c1 = Counter({'python':4,'java':5})
        print(c1.keys())
        print(c1.values())  #dict_values([4, 5])
        c1['python'] = 6  # changing count value of 'python' to 6
        print(c1.keys())
        print(c1.values()) # dict_values([6, 5])

        # using key args
        # setting count value for red and blue
        c2 = Counter(red=3,blue=5)
        print(c2.keys())
        print(c2.values()) # dict_values([3, 5])


        # count(value) of missing element(key) is zero
        print(c2['yellow']) # 0


        # most_common(n) : number of elements to display
        print(Counter(red=100,yellow=50,gree=10).most_common(1)) # return single most common element
        # output : most_common : red=100
