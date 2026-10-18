class SubarraySumEqualsK:
    def subarraySum(self,nums:list[int],k:int)->int:
        res=0
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                if s==k:
                    res +=1
        return res
    def subarraySum2(self,nums:list[int],k:int)->int:
        res=0
        smap={0:1}
        s=0
        for num in nums:
            s +=num
            diff =s-k
            res +=smap.get(diff,0)
            smap[s]=smap.get(s,0)+1
        return res

   


if __name__ =='__main__':
    obj =SubarraySumEqualsK()
    nums = [2,-1,1,2]
    k = 2
    print(obj.subarraySum2(nums,k))
    nums = [4,4,4,4,4,4]
    k = 4
    print(obj.subarraySum2(nums,k))

