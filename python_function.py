# function in python
# what about len()

# below are the examples of inbuilt function
# list1 =[1,2,3,4,5,6]
# print("maximum number in list1:",max(list1))
# print("minimum number in list1:",min(list1))
# print("sum of list1:",sum(list1))

# how do functions works?
# they may or may not accepts input parameter
# they may or may not return any output

# example of a function which doesn't accept any parameter
# and doesn't return anything
def welcome_message():
    print("welcome to iNeuron Batch-2!!!")
    
welcome_message()

# example of a function which doesn't accept any parameter
# and does return something
def bot_message():
    return "message from bot !!"

print(bot_message())

# example of a function which accepts some parameter
# and return the values
def avg_of_two_nums(a,b):
    avg_results = (a+b)//2
    return avg_results

num1 = 10
num2 = 15
output = avg_of_two_nums(num1,num2)
print("result of avg_of_two_nums :",output)

# write a function to calculate the factorial of a num?
def fact(n):
    if n==0 or n==1:
        return 1
    
    fact =1
    for num in range(n,1,-1):
        fact =num*fact
    return fact


a = 5
result = fact(a)
print(result)

# Note:- a,b,c=2,3,4
# it means we are assigning a=2,b=3,c=4...above is also the one way f  assigning the variable

# how to return mutiple values from function

def square_and_cube(n):
    sqr = n*n
    cube = n*n*n

    return sqr,cube

num = 3
sqr_ans , cube_ans = square_and_cube(num)
print('square of',num,"is",sqr_ans)
print("cube of ",num,"is",cube_ans)

# how to create optional arguments in python functions
def multiply(a,b=3):
    result =a*b
    return result

num1 =5
num2= 10
print(multiply(num1,num2))
print(multiply(num1))#here only one argument is passing,so b will works as a optional argument
print(multiply(num2))# what ever we give to argument on calling they will assign from left to right in function defintion
                    #  so num2 will assign to a, and the output will be 30

# what if we reverse this part
# its not possible 

# def multiply(a=3,b):
#     result =a*b
#     return result

# num1 =5
# num2= 10
# print(multiply(num1,num2))
# print(multiply(num1))
# print(multiply(num2))
# whatever we made optional we will do it to the last of function declaration

# Non-key valued arguments
def example_nonkeyed_args(*argv):# *argv works as list ,what input it will get converted into list
    for param in argv:
        print(param)

example_nonkeyed_args("hello","welcome")

# key value type of arguments in python
def example_of_kwargs(**kwargs):# **kwargs works as dictionary,what input it will get converted into dictionary
    for k,v in kwargs.items():
        print("key is:",k,"and","value is:",v)



example_of_kwargs(hosts='170.80.80.80',port=9021,pswd='xxfgh')