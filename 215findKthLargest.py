def findKthLargest(nums, k):
    nums.sort()
    print nums[0-k]

findKthLargest([1,2,3,4,5], 3)