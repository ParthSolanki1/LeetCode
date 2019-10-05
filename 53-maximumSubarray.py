def maxSubArray(nums):
    sum = nums[0]
    arr = [sum]
    for i in range(1, len(nums)):
        sum = max(nums[i], nums[i]+sum)
        arr.append(max(nums[i], nums[i]+arr[i-1]))

    return max(arr)