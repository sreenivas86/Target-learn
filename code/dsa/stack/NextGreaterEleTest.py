def numstest(nums:list[int])->list[int]:
    res=[-1]*len(nums)
    stack:list[int]=[]
    for i in range(len(nums)-1,-1,-1):
        cur=nums[i]
        while stack and cur> nums[stack[-1]]:
            stack.pop()
        if stack :
            res[i]=stack[-1]
        stack.append(i)

    return res


nums1 = [4,1,2]
print(numstest(nums1))
nums2 = [1,3,4,2]
print(numstest(nums2))


