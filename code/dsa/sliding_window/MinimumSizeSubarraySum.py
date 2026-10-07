class MinimumSizeSubarraySum:
    def minimumSizeSubarraySum(self,target:int,nums:list[int])->int:
        res=float('inf')
        n=len(nums)
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum +=nums[j]
                if sum>=target:
                    res= min(res,j-i+1)


        return 0 if res==float('inf') else int(res)
    # method 2: Dynamic sliding window with two pointers
    def minimumSizeSubarraySum2(self,target:int,nums:list[int])->int:
        l,total=0,0
        res=float('inf')
        for r in range(len(nums)):
            total +=nums[r]
            while total >= target:
                res=min(res,r-l+1)
                total -=nums[l]
                l+=1

        return 0 if res==float('inf') else int(res)



if __name__ =='__main__':
    obj= MinimumSizeSubarraySum()
    target = 10
    nums = [2,1,5,1,5,3]
    print(f'Minimum size of sub array {obj.minimumSizeSubarraySum2 (target,nums)}')
    target = 5
    nums = [1,2,1]
    print(f'Minimum size of sub array {obj.minimumSizeSubarraySum2 (target,nums)}')
