'''
given a list of integers , find the 4 integers in the list such that their
sum is closest to a target given. [No duplicates].
# [4,2,3,1,7,12] , target = 28 🡪 integers = [12,4,3,7].
'''
def find_four_closest(nums, target):
    nums.sort() 
    closest_sum = float('inf') 
    n = len(nums)
    result = []
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1  
            right = n - 1
            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                    result = [nums[i], nums[j], nums[left], nums[right]]
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
    return result
nums= [4,2,3,1,7,12]
target=28
AA=find_four_closest(nums, target)
print(AA)