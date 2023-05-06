'''
1 write a program to get the count of even numbers in a given list.
Make use of the lambda expression. # [5,7,7,8,8,8,10] 🡪 4
'''
numbers = [5,7,7,8,8,8,10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
count = len(even_numbers)
print("The count of even numbers is:", count)