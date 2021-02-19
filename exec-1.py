def message(data):
  return("My name is {} and my Mang Inasal count is {}".format(*data))

my_tuple = ('JC', 3)
my_list  = ['JC', 3]
my_set   = {'JC', 3}

print(message(my_tuple))
print(message(my_list))
print(message(my_set))
