class MaximumAverageSubarray1:
    #method 1: brute force
    def maxAvgSubarray(self, nums:list[int],k:int)->float:
        maxAvg=float('-inf')
        for i in range(len(nums)):
            j=i+1
            sum=nums[i]
            while j<i+k and i+k<=len(nums):
                sum+=nums[j]
                j+=1
            avg=sum/k
            maxAvg=max(maxAvg,avg)
        

        return maxAvg
    # method 2:
    def maxAvgSubarray2(self,nums:list[int],k:int)->float:
        return 0
    # method 3:
    def maxAvgSubarray3(self,nums:list[int],k:int)->float:
        return 0


if __name__ =="__main__":
    obj =MaximumAverageSubarray1()
    nums = [1,12,-5,-6,50,3] 
    k = 4
    print(f'maximum average is {obj.maxAvgSubarray(nums,k)}')
    nums = [5]
    k =1
    print(f'maximum average is {obj.maxAvgSubarray(nums,k)}')