class FindPivotIndex:
    def findPivotIndex(self,nums:list[int])->int:
        
        for i in range(len(nums)):
            left_sum=right_sum=0
            for j in range(i):
                left_sum +=nums[j]
            for j in range(i+1,len(nums)):
                right_sum +=nums[j]
            if left_sum == right_sum:
                return i            
        return -1
    # method 2: prefix and suffix sum 
    def findPivotIndex2(self,nums:list[int])->int:
        n=len(nums)
        prefix_sum=[0]*(n+1)
        for i in range(n):
            prefix_sum[i+1] =prefix_sum[i]+nums[i]
        for i in range(n):
            leftSum= prefix_sum[i]
            rightSum=prefix_sum[n]-prefix_sum[i+1]
            if leftSum==rightSum:
                return i
        return -1
    # method 3: prefix suffix sum optimal
    def findPivotIndex3(self,nums:list[int])->int:
        totalSum=sum(nums)
        leftSum=0
        for i  in range(len(nums)):
            rightSum=totalSum-leftSum-nums[i]
            if leftSum ==rightSum:
                return i
            leftSum +=nums[i]
        return -1

if __name__ =='__main__':
    obj =FindPivotIndex()
    nums = [1,7,3,6,5,6]
    print(f'pivot index {obj.findPivotIndex3(nums)}')
    nums= [1,2,3]
    print(f'pivot index {obj.findPivotIndex3(nums)}')
    nums=[2,1,-1]
    print(f'pivot index {obj.findPivotIndex3(nums)}')
