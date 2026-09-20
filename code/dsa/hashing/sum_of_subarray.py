


class SumOfSubarray:

    def sumOfSubArrayK1(self,nums:list[int],k:int)-> int:
        res=0
        for i in range(len(nums)):
            sum:int =0
            for j in range(i,len(nums)):
                sum +=nums[j]
                if sum== k:
                    res +=1
        return res
    # method 2: hashmap
    def sumOfSubArrayK2(self,nums:list[int],k:int)->int:
        res=prevSum=0
        seen={0:1}
        for num in nums:
            prevSum +=num
            diff=prevSum-k

            res += seen.get(diff,0) # check diff(prevSum,k) is seen in previous
            seen [prevSum] =seen.get(prevSum,0)+1
        return res


if __name__ =="__main__":
    obj= SumOfSubarray()
    nums = [1,1,1]
    k = 2
    print(f'count: {obj.sumOfSubArrayK2(nums,k)}')
    nums = [1,2,3]
    k = 3
    print(f'count: {obj.sumOfSubArrayK2(nums,k)}')