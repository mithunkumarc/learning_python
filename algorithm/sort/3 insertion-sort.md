#### logic : take incremental size of list and sort it
#### taking smallest number and inserting according to its order
#### insertion sort

      l = [6,5,3,1,8,7,2,4]
      for i in range(len(l)):
          print(l)
          for j in range(i+1):
              if l[j] > l[i]:
                  temp = l[j]
                  l[j] = l[i]
                  l[i] = temp
      print(l)


big O : n^2
