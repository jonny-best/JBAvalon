# TODO решить с помощью list comprehension и распечатать его
from pprint  import pprint

#pprint({1:{val for val in enumerate(range(10))},
#    3:list(range(15)),
#    4:4}
#)
a = [{'bin': bin(val), 'dec': val, 'hex': hex(val), 'oct': oct(val)} for val in range(16)]
#a = []
#for val in range(16):
#    a.append({'bin': bin(val),
#    'dec': val,
#    'hex': hex(val),
#    'oct': oct(val)})
pprint(a)