from collections import defaultdict


class LongestConsecutiveSequence:
    # method 1: brute force
    def longestConsecutiveSequence1(self,nums:list[int])->int:
        res=0
        unique=set(nums)
        for num in nums:
            streak,cnt=0,num
            while cnt in unique:
                cnt +=1
                streak +=1
            res =max(res,streak)
        return res

    # method 2: sorting
    def longestConsecutiveSequence2(self,nums:list[int])->int:
        if not nums:
            return 0
        res=0
        nums.sort()
        streak,curr=0,nums[0]
        i=0
        while i<len(nums):
            if curr !=nums[i]:
                curr=nums[i]
                streak =0
            while i<len(nums) and curr==nums[i]:
                i +=1
            streak +=1
            curr +=1
            res=max(res,streak) 


        return res

    # method 3: Hash set
    def longestConsecutiveSequence3(self,nums:list[int])->int:
        numSet=set(nums)
        longest =0
        for num in numSet:
            if (num-1) not in numSet:
                length=1
                while (num+length) in numSet:
                    length +=1
                longest =max(longest,length)
        return longest
    # method 4: Hashmap
    def longestConsecutiveSequence4(self,nums:list[int])->int:
        mnp=defaultdict(int)
        res =0
        for num in nums:
            if not mnp[num]:
                mnp[num] =mnp[num-1] +mnp[num+1] +1
                mnp[num - mnp[num-1]]=mnp[num]
                mnp[num + mnp[num+1]]=mnp[num]
                res= max(res,mnp[num])
        return res


# testing
if __name__ =="__main__":
    obj=LongestConsecutiveSequence()
    nums = [2,20,4,10,3,4,5]
    print(f'longest sequence is {obj.longestConsecutiveSequence4(nums)}')
    nums = [0,3,2,5,4,6,1,1]
    print(f'longest sequence is {obj.longestConsecutiveSequence4(nums)}')
