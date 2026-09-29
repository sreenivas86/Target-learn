class SubarraySumEqualsK:
    # method 1: brute force
    def subarraySumEqualsK(self,nums:list[int],k:int)->int:
        res=0
        for i in range(len(nums)):
            sum =0
            for j in range(i,len(nums)):
                sum +=nums[j]
                if sum == k:
                    res +=1
        return res
    # method 2: Hashmap
    def subarraySumEqualsK2(self,nums:list[int],k:int)->int:
        res=currSum =0
        prefixSum={0:1}
        for num in nums:
            currSum+=num
            diff = currSum -k
            res += prefixSum.get(diff,0)
            prefixSum[currSum] =1+prefixSum.get(currSum,0)

        return res



if __name__ =="__main__":
    obj = SubarraySumEqualsK()
    nums = [2,-1,1,2]
    k = 2
    print(f'count of subarrays {obj.subarraySumEqualsK2(nums,k)}')
    nums = [4,4,4,4,4,4]
    k = 4
    print(f'count of subarrays {obj.subarraySumEqualsK2(nums,k)}')