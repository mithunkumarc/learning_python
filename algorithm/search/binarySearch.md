            first : starting index
            last : ending index
            midpoint : middle index
            searchItem : 
            check first whether list[midpoint] == searchItem
              else
              check if searchItem < list[midpoint]
                        last = midpoint - 1
                    if searchItem > list[midpoint]
                        first = midpoint + 1


---

#### for binary search , first sort the list : big O : log n

            def binary_search(alist,item):
                if len(alist) == 0:
                    return False
                else:
                    midpoint = len(alist)//2
                    if alist[midpoint] == item:
                        return True
                    else:
                        if item < alist[midpoint]:
                            return binary_search(alist[:midpoint],item)
                        else:
                            return binary_search(alist[midpoint+1:],item)


            elem = 33
            l = [10,9,8,7,6,5,4,3,2,1,-1]
            l = sorted(l)
            print(binary_search(l,elem))




---

                def binarySearch(alist, item):
                    first = 0
                    last = len(alist) - 1
                    found = False
                    while first <= last and not found:
                        mid_point = (first + last) // 2
                        if alist[mid_point] == item:
                            found = True
                        else:
                            if item < alist[mid_point]:
                                last = mid_point - 1
                            else:
                                first = mid_point + 1
                    return found


                alist = [1,2,3,4,5,6,7,8,9]
                print(binarySearch(alist,7))
