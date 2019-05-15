#### deque : list-like container with fast appends and pops on either end

        from collections import deque
        d = deque()
        
        d.append('hello') # append right
        d.append('world') # append right
        d.appendleft('python')
        print(d)
        
        d.pop() # remove right : 'world'
        d.popleft() # remove left : 'python'
        print(d) # remaining : 'hello'


####  rotate(n=1) : Rotate the deque n steps to the right.

        from collections import deque
        d = deque()
        d.append(1)
        d.append(2)
        d.append(3)
        print(d)
        d.rotate(1)
        print(d)
        d.rotate(1)
        print(d)

        output : 

        deque([1, 2, 3])
        deque([3, 1, 2])
        deque([2, 3, 1])
