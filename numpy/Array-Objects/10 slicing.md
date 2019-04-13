synatax : var[starting_row: ending_row+1 : step]

          c = np.arange(1,26).reshape(5,5)

          c

          array([[ 1,  2,  3,  4,  5],
                 [ 6,  7,  8,  9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25]])


        c[0:1] # selecting only 0th row

        output : array([[1, 2, 3, 4, 5]])


        c[0::2] # selection all rows but with interval of 2 , alternate rows are selected

        array([[ 1,  2,  3,  4,  5],
               [11, 12, 13, 14, 15],
               [21, 22, 23, 24, 25]])
