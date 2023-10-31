'''
  use | operator
  or
  use ** spread operator
'''
colorsCode = {"red": 1, "green": 2, "blue": 3}
anotherColorCode = {"black": 4, "white": 5, "yellow": 6}
print(colorsCode | anotherColorCode)
print({**colorsCode, **anotherColorCode})
