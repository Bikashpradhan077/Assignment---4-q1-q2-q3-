# Write a Python program to square the elements of a list using map() function.
#Sample List: [4, 5, 2, 9]
# Square the elements of the list:
#[16, 25, 4, 81]
#                                   ANSWER

list1 = [4,5,2,9]
print("Sample list : ", list1)
square_list = map(lambda x: x*x, list1) 
print("Square the elements of the list : ")
print(list(square_list))