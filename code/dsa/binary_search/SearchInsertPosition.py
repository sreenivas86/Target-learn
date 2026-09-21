import bisect
class SearchInsertPosition:
    # method 1: normal for loop
    def searchInsertPosition(self, nums:list[int], target:int)->int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)
    # method 2: using binary search 1
    def searchInsertPosition2(self,nums:list[int],target:int)->int:
        res=len(nums)
        l=0
        r=len(nums)-1
        while l<r:
            mid =(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                res=mid
                r=mid-1
            else :
                l=mid+1
        return res
    # method 4: Binary search II
    def searchInsertPosition3(self,nums:list[int],target:int)->int:
        
        l=0
        r=len(nums)
        while l<r:
            mid =(l+r-1)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                r=mid
            else :
                l=mid+1
        return l

    # method 4: lower bound
    def searchInsertPosition4(self,nums:list[int],target:int)->int:
        l=0
        r=len(nums)
        while l<r:
            m= (l+r)//2
            if nums[m]>=target:
                r=m
            elif nums[m]<target:
                l=m+1
        return l
    
    # method 5: inbuilt method
    def searchInsertPosition5(self,nums:list[int],target:int)->int:
        return bisect.bisect_left(nums,target)
    

if __name__ =='__main__':
    obj=SearchInsertPosition()
    nums = [1,3,5,6]
    target = 5
    print (f'{target} is position {obj.searchInsertPosition5(nums,target)}')
    nums = [1,3,5,6]
    target = 2
    print (f'{target} is position {obj.searchInsertPosition5(nums,target)}')
    nums = [1,3,5,6]
    target = 7
    print (f'{target} is position {obj.searchInsertPosition5(nums,target)}')

