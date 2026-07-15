nums = [1, [2, 3], [4, [5, [6, [7]]]]]

def flatten(nums, result=None):
    if result is None:
        result = []
    for i in nums:
        if isinstance(i, int):
            result.append(i)
        else:
            flatten(i, result)
    return result

print(flatten(nums))
