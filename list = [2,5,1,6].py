
list1= [4, 3, 6, 12, 15]
list2 =[3, 4, 8, 9, 12]

print( '1st list:',list1)
print('2nd list:',list2)

combained_list=[ i + j for i, j in zip(list1, list2)]

print ('Concatenate two lists index-wise:',combained_list)


list1.insert(2, "33")