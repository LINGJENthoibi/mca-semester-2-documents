from collections import deque
nums = deque([1,2,3,4,5])
nums.rotate(1)
print(list(nums))

nums.rotate(-1)
print(list(nums))
