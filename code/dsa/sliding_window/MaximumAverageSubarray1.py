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
    # method 2: using prefix sum
    def maxAvgSubarray2(self,nums:list[int],k:int)->float:
        if k>len(nums):
            return -1
        # prefix sum 
        pref_sum=[0]*len(nums)
        pref_sum[0]=nums[0]
        for i in range(1,len(nums)):
            pref_sum[i]=pref_sum[i-1]+nums[i]
        # use sliding window
        maxAvg=pref_sum[k-1]/k
        for i in range(k,len(nums)):
            curr_sum=pref_sum[i]-pref_sum[i-k]
            curr_avg=curr_sum/k
            maxAvg= max(maxAvg,curr_avg)
        return maxAvg
    # method 3: using sliding window O(n)and O(1)
    def maxAvgSubarray3(self,nums:list[int],k:int)->float:
        if k>len(nums):
            return -1
        # first caluculate sum of first k elements
        sum=0
        for i in range(k):
            sum+=nums[i]
        max_avg= sum/k
        for i in range(k,len(nums)):
            sum =sum +nums[i]-nums[i-k]
            curr_avg=sum/k
            max_avg=max(max_avg,curr_avg)
        return max_avg


if __name__ =="__main__":
    obj =MaximumAverageSubarray1()
    nums = [1,12,-5,-6,50,3] 
    k = 4
    print(f'maximum average is {obj.maxAvgSubarray3(nums,k)}')
    nums = [5]
    k =1
    print(f'maximum average is {obj.maxAvgSubarray3(nums,k)}')