#### map filter and reduce functions expects a lambda function and sequence

### map()

            One of the common things we do with list and other sequences is applying an operation 
            to each item and collect the result.

            The map(aFunction, aSequence) function applies a passed-in function to each item in an
            iterable object and returns a list containing all the function call results.

            items = [1, 2, 3, 4, 5]

            def sqr(x):
                return x**2

            newItems = map(sqr, items)
            print(list(newItems))
            # [1, 4, 9, 16, 25]


            ---or--- using lambda

            items = [1, 2, 3, 4, 5]
            sqr = lambda x:x**2
            newItems = map(sqr, items)
            print(list(newItems))
            # [1, 4, 9, 16, 25]


---


#### filter : As the name suggests filter extracts each element in the sequence for which the function returns True.

            # filter even numbers
            items = [1, 2, 3, 4, 5]

            def even(x):
                if x%2 == 0:
                    return x

            newItems = filter(even, items)
            print(list(newItems))
            # output : [2,4]


            --or-- using lambda function

            # filter even numbers
            items = [1, 2, 3, 4, 5]
            even = lambda x : x%2==0
            newItems = filter(even, items)
            print(list(newItems))
            # output : [2,4]


---


#### reduce() : This function reduces a list to a single value by combining elements via a supplied function. 



            import functools
            items = [1, 2, 3, 4, 5]

            def sum(x,y):
                return x + y

            totalSum = functools.reduce(sum, items)
            print(totalSum)
            # output : 15



            --or-- using lambda

            import functools
            items = [1, 2, 3, 4, 5]

            sum = lambda x,y:x+y
            totalSum = functools.reduce(sum, items)
            print(totalSum)
            # output : 15


---

#### lambda with function


        def square(x):
            return x**2

        s = lambda x:function(x)

        print(5)



---

#### builtin function sum()

        sum([1,2,3]) : sum of all elements

---

#### Partial functions allow us to fix a certain number of arguments of a function and generate a new function.


        from functools import partial

        def install_os(mode,os):
            print(f'installing {os} in mode {mode}')

        install = partial(install_os, 'usb')
        install('windows')

##### partial function example

        NetSalary = GrossSalary - IncomeTax - PublicProvidentFund - ProfessionalTax

        def calculate_netsalary(income_tax,proffessional_tax, public_provident_fund,gross_salary):
            return gross_salary - income_tax - proffessional_tax - public_provident_fund

        netsalary = partial(calculate_netsalary, 1000, 500,2000)
        print(f'net salary {netsalary(50000)}')
        print(f'net salary {netsalary(40000)}')


******************************************************************************************
