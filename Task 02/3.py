'''
Problem 3 🡪 Take from user x number and prints the factorial of
number X. # input: 5, output: 120
'''
num=int(input("Enter a number: "))
factorial=1
if(num==0):
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
       factorial = factorial*i
    print("The factorial of",num,"is",factorial)
