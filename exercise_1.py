tups = ('fonsy', 5)
sets = {'fonsy', '5'}
lists = ['fonsy', 5]
dictionaries = dict(name= 'fonsy', rice= 5)

print("My name is {} and my Mang Inasal rice record is {}.".format(*tups))
print("My name is {} and my Mang Inasal rice record is {}.".format(*sets))
print("My name is {} and my Mang Inasal rice record is {}.".format(*lists))
print("My name is {name} and my Mang Inasal rice record is {rice}.".format(**dictionaries))