'''
Problem 4 🡪 Take from the user a list and remove duplicated items then print it
# Sample input : [“Somia”,”Abdulrhman”,”Manel”,”Abdulrhman”]
# Sample output: [“Somia”,”Abdulrhman”,”Manel”]
'''
list = input("Enter a list of items, separated by commas: ").split(",")
# Somia,Abdulrhman,Manel,Abdulrhman
unique_list = list(set(list))  
print(unique_list)