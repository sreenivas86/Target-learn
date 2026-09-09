

class TwoSum:
    # Best approch:Time complexity O(n)
    def twoSum1(self,nums:list[int],target:int)-> list[int]:
        seen=list()
        for index, num in enumerate(nums):
            compliment=target-num
            if compliment in seen:
                return [seen.index(compliment),index]
            seen.append(num)
        return []
    #  Brute force approch
    
    def twoSum2(self,nums:list[int], target:int)-> list[int]:
        n=len(nums)
        for i in range(n):
            complement= target-nums[i]
            for j in range (i+1, n):
                if complement== nums[j]:
                    return [i,j]
            
            return []
    
    # Two pointer 
    def twoSum3(self, nums:list[int], target:int)-> list[int]:
        nums.sort()
        first=0
        last=len(nums)-1
        while(first<last):
            if (nums[first] +nums[last])== target:
                return [first,last]
            elif (nums[first]+ nums[last]) >target:
                last -=1
            else :
                first+=1
        return []

   
# test code
if __name__ =='__main__':
    obj =TwoSum()
    nums=[2,7,11,15]
    target=9
   
    print(f'approch 1 {obj.twoSum1(nums,target)}')
    print(f'approch 2 {obj.twoSum2(nums,target)}')
    print(f'approch 3 {obj.twoSum3(nums,target)}')
