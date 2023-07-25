Generators are special iterators that can only be iterated through one
time. Generators are created with special generator functions.

when you call Generator function, it returns gen obj, which is iterable only once.
if you want to loop again, create new gen obj by calling Generator function again.
