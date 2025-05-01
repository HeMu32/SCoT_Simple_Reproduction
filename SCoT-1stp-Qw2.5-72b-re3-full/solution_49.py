def specified_element(nums, N):
    result = []
    for sublist in nums:
        if len(sublist) > N:
            result.append(sublist[N])
        else:
            result.append(None)
    return result