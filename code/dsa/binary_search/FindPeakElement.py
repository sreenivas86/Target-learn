class FindPeakElement:
    # bruteforce

    def findPeak(self,nums:list[int])->int:
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return i

        return len(nums)-1

    # method 2: binary search
    def findPeak2(self,nums:list[int])->int:
       
        l=0
        r=len(nums)-1

        while l<=r:
            mid =(l+r)//2
            if mid >0 and nums[mid]<nums[mid-1]:
                r = mid-1
            elif mid< len(nums)-1 and nums[mid]<nums[mid+1]:
                l = mid +1
            else :
                return mid


if __name__ =='__main__':
    obj =FindPeakElement()
    nums = [1,2,3,1]
    print(obj.findPeak2(nums))

    nums = [1,2,1,3,4,5,0]
    print(obj.findPeak2(nums))
