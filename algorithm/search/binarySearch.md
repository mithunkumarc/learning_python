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
