class MaxConsecutiveOnesIII:
    # method1: Broute force mthod
    def longestOnes(self, nums:list[int], k:int)->int:
        res=0
        for i in range(len(nums)):
            zeros=0
            for j in range(i,len(nums)):
                if nums[j] ==0:
                    zeros +=1
                if zeros>k:
                    break
                res=max(res,j-i+1)

        return res
    # method 2: Dynamic sliding window optimal
    def longestOnes2(self,nums:list[int],k:int)->int:
        res,zeros=0,0
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros +=1
            while zeros >k:
                if nums[left]==0:
                    zeros -=1
                left +=1
            res =max(res,right-left+1)
        return res



if __name__ =="__main__":
    obj=MaxConsecutiveOnesIII()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(obj.longestOnes2(nums,k))

    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(obj.longestOnes2(nums,k))