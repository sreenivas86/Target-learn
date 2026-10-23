import bisect
class FirstAndLastPositionOfElement:
    # bruteforce method
    def firstAndLastPosition(self,nums:list[int],target:int)->list[int]:
        first=last=-1
        for i,num in enumerate(nums):

            if num == target:
                if  first ==-1:
                    first=i
                last =i
        return [first,last]
    # binary search
    def firstAndLastPosition2(self,nums:list[int],target:int)->list[int]:
 
        def findIndex(nums:list[int],target:int,bais:bool)->int:
            left=0
            right= len(nums)-1
            res =-1
            while left<=right:
                mid = (left+right)//2
                if nums[mid] > target:
                    right =mid -1
                elif nums[mid] <target:
                    left = mid +1
                else :
                    if bais:
                        right = mid -1
                        res =mid
                    else :
                        res =mid
                        left =mid +1

            return res

        left=findIndex(nums,target,True)
        right =findIndex(nums,target,False)
        
        return [left,right]

    # inbuilt method
    def firstAndLastPosition3(self,nums:list[int],target:int)->list[int]:
        left= bisect.bisect_left(nums,target)
        if left >= len(nums) or nums[left] !=target:
            return [-1,-1]
        right= bisect.bisect_right(nums,target)-1
        return [left,right]
        

        


if __name__ =='__main__':
    obj= FirstAndLastPositionOfElement()

    nums = [5,7,7,8,8,10]
    target = 8
    #Output: [3,4]
    print(obj.firstAndLastPosition3(nums,target))

    nums = [5,7,7,8,8,10]
    target = 6
    #Output: [-1,-1]
    print(obj.firstAndLastPosition3(nums,target))
    
    nums = [5,7,7,8,8,10]
    target = 8
    #Output: [3,4]
    print(obj.firstAndLastPosition3(nums,target))
    nums = [1]
    target = 1
    # Output: [0,0]
    print(obj.firstAndLastPosition3(nums,target))
    