class ContainsDuplicate:
    #BruteForce method 
    def containsDuplicate1(self,nums:list[int])-> bool:
        n=len(nums)
        for i,num in enumerate(nums):
            for j in range(i+1,n):
                if num==nums[j]:
                    return True
        return False
    
    # best approch
    def containsDuplicate2(self,nums:list[int])-> bool:
        seen= set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    

# main method
if __name__ == "__main__":
    obj = ContainsDuplicate()
    nums= [2,7,11,15,3,2]
    print(f'approch {obj.containsDuplicate1(nums)}')
    print(f'approch 2 {obj.containsDuplicate2(nums)}')
    
    