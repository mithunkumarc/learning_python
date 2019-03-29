#### is operator : checks two variables pointing to same object/copy
#### == operator : checks content, it doest care about same or different copies

#### lists are immutable, is and == has different meaning

>  is operator checks both variables are pointing to same copy

> == operator checks contents of two variables, it is possible that two var points to different copies

            l1 = [1,2,3]
            l2 = l1
            print(l1 == l2) # True
            print(l1 is l2) # True

            l3 = [1,2,3]
            print(l1 == l3) # content is same : True
            print(l1 is l3) # False : content may be same , but l1 and l3 are pointint to two diff copies



#### integers are immutable , is and == are same in immutable context

>  all a,b,c points to same copy, so content also same

            a = 100
            b = a
            print(a == b)   # True
            print(a is b)   # True

            c = 100
            print(a == c)   # True
            print(a is c)   # True


#### complex.conjugate() : Return the complex conjugate of its argument. (3-4j).conjugate() == 3+4j.

            c = complex(-4,5)
            print(c)                # (-4+5j)
            print(c.conjugate())    # (-4-5j)
            


            
