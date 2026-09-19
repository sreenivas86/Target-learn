



class MoveZeros:

    # method1: using extra list
    def moveZeros(self, nums:list[int])->None:
        nums2:list[int]=[]
        count=0
        for num in nums:
            if num !=0:
                count +=1
                nums2.append(num)
        for i in range(len(nums)):
            if i <len(nums2):
                nums[i]=nums2[i]
            else: 
                nums[i]=0

    # method 2: Two pointer multi pass
    def moveZeros2(self, nums:list[int])->None:
        l=0
        for i in range(len(nums)):
            if nums[i]:
                nums[l]=nums[i]
                l +=1
        while l< len(nums):
            nums[l]=0
            l +=1
    # method 3: two pointers single pass
    def moveZeros3(self, nums:list[int])->None:
        l=0
        for i in range(len(nums)):
            if nums[i]:
                nums[l],nums[i]=nums[i],nums[l]
                l +=1
    # method 4: two pointer while loop
    # Note: this method doesn't follow order
    def moveZeros4(self, nums:list[int])->None:
        l=0
        n=len(nums)
        while l<n:
            if nums[l]:
                l+=1
            else:
                nums[l],nums[n-1] =nums[n-1],nums[l]
                n-=1

        


if __name__ =='__main__':
    obj= MoveZeros()
    nums = [0,1,0,3,12]
    obj.moveZeros4(nums)
    print(nums)

    nums=[0]
    obj.moveZeros4(nums)
    print(nums)