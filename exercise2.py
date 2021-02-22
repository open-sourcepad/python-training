given = [1, 1.5, 2, 2.5, 3, 3.7, 4, 5, 6, 7]
output = []
for x in given:
    is_whole_number = x - int(x) == 0    
    if is_whole_number:
       output.append(f'PM{x}')
    elif x == 1.5:
       output.append(f'PM{x}')

print(output)
