class LongestSubarray1sdelete:
    # method 1: bruteforce method
    def longestSubarray(self,nums:list[int])->int:
        res=0
        for i in range(len(nums)):
            zero=0
            for j in range(i,len(nums)):
                if nums[j] ==0:
                    zero +=1
                if zero >1:
                    break
                res=max(res,j-i)
                
        return res
    # method 2: for loop and count mehtod
    def longestSubarray2(self,nums:list[int])-> int:
        res=0
        left=0
        zeoros=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeoros +=1
            while zeoros>1:
                if nums[left]==0:
                    zeoros -=1
                left +=1
            res =max(res,right-left)

            
        return res


if __name__ == '__main__':
    obj =LongestSubarray1sdelete()
    nums = [1,1,0,1]
    print(obj.longestSubarray2(nums))
    nums = [0,1,1,1,0,1,1,0,1]
    print(obj.longestSubarray2(nums))
    nums = [1,1,1]
    print(obj.longestSubarray2(nums))