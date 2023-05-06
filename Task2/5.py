'''
problem 5 🡪 What is the output of the following code ? why ?
print(round(6.5) - round(3.5) == 3)
'''

print(round(6.5) - round(3.5) == 3)# The output will be False
'''
The expression round(6.5) evaluates to 7, since 6.5 rounds up to the nearest integer.
The expression round(3.5) evaluates to 4, since 3.5 rounds up to the nearest integer.
Therefore, the entire expression is equivalent to 7 - 4 == 3.
However, 7 - 4 is actually equal to 3, not True.
Therefore, the entire expression evaluates to False.
'''