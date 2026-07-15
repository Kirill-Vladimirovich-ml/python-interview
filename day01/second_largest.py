def second_largest(nums):
    a = nums[0]
    b = nums[0]
    for i in range(len(nums)):
        if a < nums[i]:
            b = a
            a = nums[i]
        if b < nums[i] and b < a and a != nums[i]:
            b = nums[i]

    return b,a

