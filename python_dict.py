# Acts like a map data structure
# syntax
# {
 # 'name': "sunny",
 # 'age':22
 # 'skills':["python","java"]
# }
# key? -> int,strings
# list,tuple,set etc can't be used as key
# value?-> Anything

# Dictionary in python

# empty dictionary
dict1 ={}
print(type(dict1))

# how to insert values in dictionary
dict2 = {}
dict2['name'] = "sunny"
dict2['age']  = 22
dict2['skills'] = ['python','java']
dict2['state_visite'] =('UP' , 'Goa')
dict2[45] = "random key"



dict3 = {'color' : 'black', 'nationality': 'Indian' }
dict2['other_details'] = dict3
print(dict2)

# check the length of dictionary
print(len(dict2))  # length will be number of keys , value pair created

# how to access value of a particular key
print(dict2['name']) # we have to give the key name with dict name

# how  to print seconadary values of skills key
print(dict2['skills'][1])
# how to print the nationality from dict2
print(dict2['other_details']['nationality'])

# how to update vlaue on a particular key

dict2['age'] = 25
print(dict2['age'])

# how to get the keys from a dictionary

total_keys = list(dict2.keys())
print("total keys in dictionary :",total_keys)

# how to get values from a dictionary
total_values = list(dict2.values())
print(" total values in dictionary:",total_values)
# there is also .get method to get values

# how to iterate on dictionary

for k,v in dict2.items():
    print("keys is =",k," and value is =",v)


# compare dictionary

dict4 ={'a': 1,'b': 2, 'c': 3}
dict5 ={'b':2,'c':3,'a':1}
print(dict4==dict5) # output will true because it is not a sequential data structure.

# how to delete specific key value pair from dictionary
del dict2['age']
del dict2[45]
print(dict2)

# how to check if key exists in dictionary or not
# alternate way
keys_in_dict = list(dict2.keys())
if 'skills' in keys_in_dict:
    print(True)
else:
    print(false)
