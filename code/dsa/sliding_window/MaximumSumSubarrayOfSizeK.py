class MaximumSumSubarray:
    # method1: Bruteforce
    def maximumSubSubarray(self,nums:list[int],k:int)-> int:
        max_sum=0
        for i in range(len(nums)):
            sum=0
            j=i
            while j <i+k and i+k< len(nums):
            
                sum+=nums[j]
                j+=1
            max_sum=max(max_sum,sum)
        
        return max_sum
    # method2: prefix sum
    def maximumSubSubarray2(self,nums:list[int],k:int)-> int:
        if k>len(nums):
            return -1
        # prefix sum
        pref_sum=[0]*len(nums)
        pref_sum[0]=nums[0]
        for i in range(1,len(nums)):
            pref_sum[i]=pref_sum[i-1]+nums[i]
        maxSum=pref_sum[k-1]
        for i in range(k,len(nums)):
            curr_sum=pref_sum[i]-pref_sum[i-k]
            maxSum=max(maxSum,curr_sum)

            
        return maxSum
    # method 3: sliding window O(1) space
    def maximumSubSubarray3(self,nums:list[int],k:int)->int:
        if k>len(nums):
            return -1
        sum=0
        for i in range(k):
            sum+=nums[i]
        max_sum=sum
        for i in range(k,len(nums)):
            sum =sum+nums[i]-nums[i-k]
            max_sum=max(max_sum,sum)

        return max_sum


if __name__ =="__main__":
    obj =MaximumSumSubarray()
    nums = [1,12,-5,-6,50,3] 
    k = 4
    print(f'maximum sum is {obj.maximumSubSubarray(nums,k)}')
    nums = [5]
    k =1
    print(f'maximum sum is {obj.maximumSubSubarray3(nums,k)}')
    nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    print(f'maximum sum is {obj.maximumSubSubarray3(nums,k)}')
    nums = [100, 200, 300, 400]
    k = 1
    print(f'maximum sum is {obj.maximumSubSubarray3(nums,k)}')
    nums = [100, 200, 300, 400]
    k = 2
    print(f'maximum sum is {obj.maximumSubSubarray3(nums,k)}')
