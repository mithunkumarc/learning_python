#### selection sort
#### in each round highest element goes to last
#### in next loop, last position is skipped for comparision

        data = [33,10,9,22,8,7,6,5,11]
        size = len(data)
        while size > 1:
            for i in range(0,size):
                if (i+1) < len(data):
                    if data[i] > data[i+1]:
                        temp = data[i]
                        data[i] = data[i+1]
                        data[i+1] = temp
            print(data)
            size -= 1
        print(data)


big O : n ^ 2
