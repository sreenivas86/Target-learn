import bisect

class BinarySearch:
    #method 1: using recursion
    def binarySearch1(self, nums:list[int], target:int)-> int:
        def helper(l:int,r:int) ->int:
            if l>r:
                return -1
            mid =(l+r)//2
            if nums[mid] == target :
                return mid
            elif nums[mid]>target:
                return helper(0,mid-1)
            return helper(mid+1,r)
        return helper(0,len(nums)-1)
    # method 2: using while loop
    def binarySearch2(self, nums:list[int],target:int)->int:
        l=0
        r=len(nums)
        while l<r:
            mid = (l+r-1)//2
            if nums[mid] ==target:
                return mid
            elif nums[mid]> target:
                r=mid
            else:
                l=mid +1
        return -1
        
    # method 3: upper bound
    def binarySearch3(self,nums:list[int], target:int)->int:
        l=0
        r=len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid] >target:
                r=mid
            elif nums[mid]<=target:
                l=mid+1
        return l-1 if(l-1<len(nums)and nums[l-1]==target)  else -1
    # mehtod 4: lower bound
    def binarySearch4(self,nums:list[int],target:int)->int:
        l=0
        r=len(nums)
        while l<r:
            mid= (l+r)//2
            if nums[mid] >= target:
                r =mid
            elif nums[mid]<target:
                l= mid+1
        return l if (l<len(nums)and nums[l]==target) else -1
    
    # method 5: inbuilt method
    def binarySearch5(self,nums:list[int],target:int)->int:
        index= bisect.bisect(nums,target)
        
        return index-1 if index-1<len(nums) and nums[index-1]==target else -1
        
    
if __name__=="__main__":
    obj= BinarySearch()
    nums = [-1,0,3,5,9,12]
    target = 9
    print( "index of the target is ",obj.binarySearch5(nums,target))
    nums = [-1,0,3,5,9,12]
    target = 2
    print( "index of the target is ",obj.binarySearch5(nums,target))
    