class ProductOfSumExceptSelf:
    # method 1: Brute Force
    def productOfArray(self,nums:list[int])->list[int]:
        n=len(nums)
        res =[1]*n
        for i in range(n):
            leftProd=1
            for j in range(i):
                leftProd *=nums[j]
            rightProd=1
            for j in range(i+1,n):
                rightProd *=nums[j]
            res[i] =rightProd* leftProd
        return res
    # method 2: prefix suffix sum
    def productOfArray2(self,nums:list[int])->list[int]:
        res:list[int]=[]
        n=len(nums)
        left=[1]*n
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        right = [1]*n
        for i in range (n-2,-1,-1): 
            right[i] =right[i+1]*nums[i+1]
        for i in range(n):
            res.append(left[i]*right[i])

        return res
if __name__=="__main__":
    obj = ProductOfSumExceptSelf()
    nums = [1,2,4,6]
    print(obj.productOfArray2(nums))
    nums = [-1,0,1,2,3]
    print(obj.productOfArray2(nums))

