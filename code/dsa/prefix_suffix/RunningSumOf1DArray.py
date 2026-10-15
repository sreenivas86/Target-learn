class RunninSumOf1DArray:

    def runningSum(self,nums:list[int])->list[int]:
        n=len(nums)
        res=[0]*n
        res[0]=nums[0]

        for i in range (1,n):
            res[i]=res[i-1]+nums[i]

        return res


if __name__ =="__main__":
    obj =RunninSumOf1DArray()
    nums = [1,2,3,4]
    print(obj.runningSum(nums))
    
    nums = [1,1,1,1,1]
    print(obj.runningSum(nums))
    nums = [3,1,2,10,1]
    print(obj.runningSum(nums))
