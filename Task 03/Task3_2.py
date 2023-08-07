'''
Given a list of integers, write a function to return the index of the
target. and if not found, sort the list and return the index of the target
if it would be inserted.
# [4,2,3,1,7] , target= 3 🡪 index = 2
# [4,2,3,1,7] , target = 5 🡪 sorted = [1,2,3,4,7] , index = 4.

'''
def find_target_index(lst, target):
    if target in lst:
        return lst.index(target)
    else:
        sorted_lst = sorted(lst)
        for i in range(len(sorted_lst)):
            if target < sorted_lst[i]:
                return i
        return len(sorted_lst)
lst1 = [4, 2, 3, 1, 7]
target1 = 5
index1 = find_target_index(lst1, target1)
print(f"Index of {target1} in {lst1}: {index1}")