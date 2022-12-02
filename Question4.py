
#Given a Python list, write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]

a = set(list1)
a.remove(20)
print(a)