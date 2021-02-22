def inasalize(tuple_input):
  mang_inasal_valid = (1,1.5,2,3,4,5,6,7)
  filtered_tuple = (tuple_inasal for tuple_inasal in tuple_input if tuple_inasal in mang_inasal_valid)
  return list(filtered_tuple)

values = (1,1.5,2,2.5,3,3.7,4,5,6,7)
print(inasalize(values))
