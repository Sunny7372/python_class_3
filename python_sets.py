# sets in python

# empty set

set1 = set()
print(type(set1))

set3 ={1,2,3,4,5,2,1,4}
print(set3) # only distinct element will print

list1 = [1,2,3,4,5,6,7,8,1]
set2 = set(list1)
print(set2) # it will only print distinct element.any duplicacy will not print

# it will not work for empty set, it is just for creating empty dict
set4 ={}
print(type(set4))

# how we can iterate elements in the set

for num in set2:
    print(num)

# convert output of set into list

list1 =[1,2,3,4,1,2,3,4,5,6,7,8,1]
set5 = list(set(list1))
print(set5)

# how to insert elements in the set
set6 =set()
set6.add(1)
set6.add(1)
set6.add(2)
set6.add(5)
set6.add(2)
set6.add(1)
set6.add(2)
print(set6)

# use of update method
tmp =[1,2,3,4,5,1,2,3,4,5,1,2,3]
set6.update(tmp)
print(set6)

# calculate the length of the set
print(len(set6))

# set operations
set_a = {1,2,3,4,5,6}
set_b = {3,6,8,9,10}


# union operation
print(set_a | set_b) # keep all the elements of both sets

# intersection operation
print(set_a & set_b) # keep common elements of both sets

# A-B ?
# difference in sets
print(set_a - set_b) # keeping all the elements of set_a except those who are present in set_b
print(set_b-set_a) # keeping all the elements of set_b except those who are present in set_a

# comparison in sets
set_x = {1,2,3,4,5}
set_y = {1,2,3,5,4,5,1} # it will look like{1,2,3,4,5}
print(set_x==set_y)

set_m = {5,6,7,1,2,4} # it will look like {1,2,4,5,6,7}
print(set_m)




