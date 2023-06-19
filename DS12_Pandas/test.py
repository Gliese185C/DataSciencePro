list2 = [0,1,3,88,42,98,3,1,98,63,63,55,7,16,16,4,0,42,4,7,88]

result = 0

for element in list2:
    result = result ^ element

print(result)