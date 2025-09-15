from collections import Counter, defaultdict, OrderedDict

# li = [1,2,2,2,2,2,2,3,4,5,6,7,8,9,10]
# print(Counter(li))
# sentence = 'blah blah blah thing about python'
# print(Counter(sentence))

# dictionary = defaultdict(lambda: "does not exist", {'a':1, 'b':2, 'c':3, 'd':4, 'e':5})
# print(dictionary['c'])

# OrderedDict explicitly looks at order regardless if a 'dictionary' (unordered) or not.
# d = OrderedDict()
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
#
# d2 = OrderedDict()
# d2['a'] = 1
# d2['c'] = 3
# d2['b'] = 2


d = {'f': 100}
d['a'] = 1
d['b'] = 2
d['c'] = 3

d2 = {'f': 100}
d2['a'] = 1
d2['c'] = 3
d2['b'] = 2

print(d2 == d)
