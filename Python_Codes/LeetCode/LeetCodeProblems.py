from time import sleep
import datetime

# 1524. Number of Sub-arrays With Odd Sum
def numOfSubarrays(arr):
    count = 0
    subArrays = []
    print(datetime.datetime.now() - ex)
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subArrays.append(arr[i : j + 1])

    print(datetime.datetime.now() - ex)
    for subArray in subArrays:
        if len(subArray) == 0 and subArray[0] % 2 == 0:
            count += 1
        else:
            if sum(subArray) % 2 != 0:
                count += 1

    return count


# 1. Two Sum
def twoSum(nums, target):
    for i in nums:
        if target - i in [nums.remove(i)][0]:
            if i == target - i:
                num = nums.index(i)
                nums[nums.index(i)] = 0
                return [num ,nums.index(i)] 
            return [nums.index(i), nums.index(target - i)]
    

def addTwoNumbers(arr1, arr2):
    nums1 = ''
    nums2 = ''
    liste = []
    for i in arr1:
        nums1 += str(i)
    for j in arr2:
        nums2 += str(j)
    res = int(nums1) + int(nums2)
    return list(str(int("".join(map(str, arr1))) + int("".join(map(str, arr2)))))[::-1]


# 1749. Maximum Absolute Sum of Any Subarray
def maxAbsoluteSum(nums):
    max_value = 0
    check = 0
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            check += nums[j]
        if abs(check) > max_value:
            max_value = abs(check)
    return max_value


# 2460. Apply Operations to an Array
def applyOperations(nums):
    i = 0
    j = 0
    while True:
        if i == len(nums) - 1:
            break
        if nums[i] == nums[i+1]:
            nums[i], nums[i+1] = nums[i]*2, 0
            while True:
                if j == len(nums) - 1:
                    break
                if nums[j] == 0:
                    if nums[j+1] == 0:
                        break
                    nums[j], nums[j+1] = nums[j+1], 0
                    j = 0
                j += 1
        i += 1
    for j in range(len(nums)):
        i = 0
        while True:
            if i == len(nums) -1:
                break
            if nums[i] == 0:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 1
    return nums


# 2570. Merge Two 2D Arrays by Summing Values
def mergeArrays(nums1, nums2):
    merge = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i][0] == nums2[j][0]:
                merge.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                nums2.remove(nums2[j])
                break
            if nums2[j][0] < nums1[i][0]:
                merge.append(nums2[j])
                # nums2[j] = [99999,0]
                continue
            merge.append(nums1[i])
            break
    return merge


# nums1 = [[2,4],[3,6],[5,5]]
# nums2 = [[1,3],[4,3]]
# merge = [[1,3],[2,4],[3,6],[4,3],[5,5]]
# merge = [[1, 3], [2, 4], [1, 3], [3, 6], [1, 3], [4, 3]]

# print(mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
print(mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))