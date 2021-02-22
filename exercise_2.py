def inasalize(tuple_input):
  mang_inasal_valid = (1,1.5,2,3,4,5,6,7)
  filtered_tuple = (inasal for inasal in tuple_input if inasal in mang_inasal_valid)
  return list(map(lambda inasal: f"PM{inasal}", filtered_tuple))

values = (1,1.5,2,2.5,3,3.7,4,5,6,7)
print(inasalize(values))
