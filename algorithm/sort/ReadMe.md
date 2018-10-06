Big O : worst case
Big omega : best case
Big theta : list between , upper bound big O and lower bound omega



Big-O is a measure of the longest amount of time it could possibly take for the algorithm to complete.
 f(n) ≤ cg(n), where f(n) and g(n) are non-negative functions, g(n) is upper bound, then f(n) is Big O of g(n). 
 This is denoted as "f(n) = O(g(n))"

Big Omega describes the best that can happen for a given data size.
"f(n) ≥ cg(n)", this makes g(n) a lower bound function

Theta is basically saying that the function, f(n) is bounded both from the top and bottom by the same function, g(n).
f(n) is theta of g(n) if and only if f(n) = O(g(n)) and f(n) = Ω(g(n))
This is denoted as "f(n) = Θ(g(n))"


#### log(n) explanation : applcation divide and conquer, binary search. reducing input and operate

     Repeatedly dividing by a constant

     Take any number n; say, 16. 
     How many times can you divide n by two before you get a number less than or equal to one? For 16, we have that

     16 / 2 = 8
      8 / 2 = 4
      4 / 2 = 2
      2 / 2 = 1

     Notice that this ends up taking four steps to complete. 
     Interestingly, we also have that log2 16 = 4. Hmmm... what about 128?

     128 / 2 = 64
      64 / 2 = 32
      32 / 2 = 16
      16 / 2 = 8
       8 / 2 = 4
       4 / 2 = 2
       2 / 2 = 1

     This took seven steps, and log2 128 = 7. Is this a coincidence? Nope! There's a good reason for this. 
     Suppose that we divide a number n by 2 i times. 
     Then we get the number n / 2i. If we want to solve for the value of i where this value is at most 1, we get

         n / 2i ≤ 1

         n ≤ 2i

         log2 n ≤ i



#### practical examples of BIG 0 notation

    Practical Examples

    O ( n ) {\displaystyle O(n)} O(n): printing a list of n {\displaystyle n} n items to the screen, looking at each item once.

    O ( log 2 ⁡ n ) {\displaystyle O(\log _{2}{n})} {\displaystyle O(\log _{2}{n})}", taking a list of items, cutting it in half repeatedly until there's only one item left.

    O ( n 2 ) {\displaystyle O(n^{2})} O(n^{2}): taking a list of n items, and comparing every item to every other item.
