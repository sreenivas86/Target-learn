class ContainsDuplicate2:
    # method 1: Brute force
    def containsDuplicate(self, nums:list[int],k:int)->bool:
        for l in range(len(nums)):
            for r in range(l+1,min(len(nums),l+k+1)):
                if nums[l]== nums[r]:
                    return True
        return False
    # method 2: Hash map
    def containsDuplicate2(self,nums:list[int],k:int)->bool:
        seen:dict[int,int]={}
        for i in range(len(nums)):
            if nums[i] in seen and i-seen[nums[i]]<=k:
                return True
            seen[nums[i]]=i
        return False
    # method 3: set and sliding window
    def containsDuplicate3(self,nums:list[int],k:int)->bool:
        window:set[int]=set()
        l=0
        for r in range(len(nums)):
            if r-l>k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            window.add(nums[r])


        return False
if __name__ =='__main__':
    obj=ContainsDuplicate2()
    nums = [1,2,3,1]
    k = 3
    print( obj.containsDuplicate3(nums,k))
    nums = [2,1,2]
    k = 1
    print( obj.containsDuplicate3(nums,k))