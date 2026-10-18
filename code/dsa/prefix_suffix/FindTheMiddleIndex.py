class FindTheMiddleIndex:
    # method 1: Brute force
    def findTheMiddleIndex(self,nums:list[int])->int:
        n=len(nums)
        for i in range(n):
            leftSum=rightSum=0
            for j in range(i):
                leftSum +=nums[j]
            for j in range(i+1,n):
                rightSum +=nums[j]
            if leftSum == rightSum:
                return i
        return -1

    # method 2: prefix suffix method
    def findTheMiddleIndex2(self,nums:list[int])->int:
        n=len(nums)
        prefix_sum=[0]*(n+1)
        for i in range(n):
            prefix_sum[i+1] =prefix_sum[i]+nums[i]
        for i in range(n):
            rightSum=prefix_sum[n] -prefix_sum[i+1]
            if prefix_sum[i] == rightSum:
                return i

        return -1
    # method 3: prefix suffix method optimal
    def findTheMiddleIndex3(self,nums:list[int])->int:
        totalSum=sum(nums)
        leftSum=0
        for i in range(len(nums)):
            rightSum =totalSum -leftSum -nums[i]
            if rightSum ==leftSum:
                return i
            leftSum +=nums[i]

        return -1


if __name__ =='__main__':
    obj =FindTheMiddleIndex()
    nums = [2,3,-1,8,4]
    print (obj.findTheMiddleIndex3(nums))
    nums = [1,-1,4]
    print (obj.findTheMiddleIndex3(nums))
    nums = [2,5]
    print (obj.findTheMiddleIndex3(nums))
