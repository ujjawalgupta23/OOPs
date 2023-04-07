# applies a function to each item in an iterable(list, tuple)
from functools import reduce

store = [("shirt", 20),
         ("pants", 25),
         ("jacket", 50),
         ("socks", 10)]

to_inr = lambda data: (data[0], data[1] * 82)
store_inr = list(map(to_inr, store))
print(store_inr)


ages = [12, 55, 22, 21, 1, 5]
eligible = list(filter(lambda age: age >= 18, ages))
print(eligible)


fact = reduce(lambda x, y: x * y, range(5, 1, -1))
print(fact)
