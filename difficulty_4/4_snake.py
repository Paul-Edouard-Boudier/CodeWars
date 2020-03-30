def snail(snail_map):
    arr = []
    while snail_map:
        i_max = len(snail_map[0])-1
        
        arr.extend(snail_map[0])
        del snail_map[0]
        if not snail_map:
            return arr
        
        for i in range(len(snail_map)):
            arr.append(snail_map[i][i_max])
            del snail_map[i][i_max]
        if not snail_map:
            return arr
            
        arr.extend(snail_map[-1][::-1])
        
        del snail_map[-1]
        if not snail_map:
            return arr
        
        for l in reversed(range(len(snail_map))):
            arr.append(snail_map[l][0])
            del snail_map[l][0]

    return arr
    
    
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
# print(snail(array) == expected)
array_two = [[1,2,3,5],
             [4,5,6,7],
             [7,8,9,2],
             [5,3,6,1]]
expected_two = [1,2,3,5,7,2,1,6,3,5,7,4,5,6,9,8]
# print(v2(array_two) == expected_two)
print(expected)
print(v2(array))

print(expected_two)
print(v2(array_two))    
 