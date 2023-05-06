'''
Problem 2 🡪 Take from user three numbers A, B, and C, and print them in
ascending order in one line.
# Sample input: 9 5 6 , Sample output: 5 6 9
'''
numA=int(input("Enter a number A: "))
numB=int(input("Enter a number B: "))
numC=int(input("Enter a number C: "))
sorted_num = sorted([numA, numB, numC])
result = " ".join(map(str, sorted_num))
print(result)