#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
#sample input: 10
#sample output: 35
#                                         ANSWER
x=int(input("Sample input : "))
y = lambda x : x + 25
print("Sample output : ",y(x))