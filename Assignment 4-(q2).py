
# Write a Python program to triple all numbers of a given list of integers. Use Python map.
#sample list: [1, 2, 3, 4, 5, 6, 7]
#Triple of list numbers:
#[3, 6, 9, 12, 15, 18, 21]
#                               ANSWER

list1 = [1,2,3,4,5,6,7]
print("Sample list : ", list1)
triple_list = map(lambda x : x*3,list1) 
print("Triple of list numbers are : ")
print(list(triple_list))