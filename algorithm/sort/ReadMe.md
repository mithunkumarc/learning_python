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
