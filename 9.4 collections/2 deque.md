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
