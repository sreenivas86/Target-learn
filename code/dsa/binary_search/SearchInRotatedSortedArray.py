class SearchInRotatedSortedArray:
    # Binary search
    def search(self,nums:list[int],target:int)-> int:
        left =0
        right=len(nums)-1
        while left <=right:
            mid=(left+right)//2
            numMid=nums[mid]
            if numMid ==target :
                return mid
            elif nums[left]<=numMid :
                if nums[left]<= target<numMid:
                    right =mid-1
                else :
                    left =mid+1
                
            else:
                if numMid < target <= nums[right]:
                    left =mid +1
                else:
                    right =mid -1
                


        return -1


if __name__ =="__main__":
    obj=SearchInRotatedSortedArray()
    nums = [3,4,5,6,1,2]
    target = 1
    print (obj.search(nums,target))
    nums = [3,5,6,0,1,2]
    target = 4
    print (obj.search(nums,target))
    nums = [4,5,6,7,0,1,2]
    target = 0
    print (obj.search(nums,target))
    nums = [4,5,6,7,0,1,2]
    target = 3
    print (obj.search(nums,target))
    nums = [1]
    target = 0
    print (obj.search(nums,target))