class RemoveElement:
    # method1: brute force
    def removeElement1(self,nums:list[int], val:int) -> int:
        nums2:list[int]=[]
        for num in nums:
            if num!= val:
                nums2.append(num)
        nums[:]=nums2
        return len(nums2)
    
    # method2: Two pointers
    def removeElement2(self,nums:list[int], val:int) -> int:
        c=0
        for num in nums:
            if num !=val:
                nums[c]=num
                c +=1

        return c
    
    # method 3: Two pointers II
    def removeElement3(self,nums:list[int], val:int) -> int:
        s=0
        e=len(nums)
        while s<e:
            if nums[s]==val:
                nums[s]=nums[e-1]
                e -=1
            else:
                s +=1        
        return s

if __name__=="__main__":
    obj=RemoveElement()
    nums = [3,2,2,3]
    val = 3
    unique=obj.removeElement3(nums,val)
    print(f'unique elements: {unique} \nafter remvoe {val}: {nums[:unique]}')

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    unique=obj.removeElement3(nums,val)
    print(f'unique elements: {unique} \nafter remvoe {val}: {nums[:unique]}')