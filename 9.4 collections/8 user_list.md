#### sublclass list

        from collections import UserList

        class MyList(UserList):
            def __setitem__(self, key, value):
                self.append(value)

        m = MyList()

        for i in range(0,10):
            #m[i] = i
            # or
            m.append(i)

        print(m)
        
        output ; [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
