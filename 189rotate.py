def rotate(nums,k):
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]
rotate([1,2], 1)