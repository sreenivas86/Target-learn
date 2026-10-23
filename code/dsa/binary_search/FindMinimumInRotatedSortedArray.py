class FindMinInRotatedSortedArray:
    def findMin(self,nums:list[int])->int:
        left= 0
        right = len(nums)-1
        
        while left <right:
            mid =(left + right)//2
           
            if nums[mid]> nums[right]:
                left =mid +1
            else :
                right =mid


        return nums[left]


    



if __name__ =='__main__':
    obj =FindMinInRotatedSortedArray()
    nums = [3,4,5,6,1,2]
    print(obj.findMin(nums))
    nums = [4,5,0,1,2,3]
    print(obj.findMin(nums))
    nums = [4,5,6,7]
    print(obj.findMin(nums))