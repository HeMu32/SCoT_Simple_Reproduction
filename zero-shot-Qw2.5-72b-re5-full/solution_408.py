from heapq import nsmallest

def k_smallest_pairs(nums1, nums2, k):
    return nsmallest(k, ((u, v) for u in nums1 for v in nums2), key=sum)