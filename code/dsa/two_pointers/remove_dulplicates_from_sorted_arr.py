
from enum import unique


class RemoveDuplicates:
    # method 1: using list
    def removeDuplicates(self, nums:list[int])-> int:
        unique:list[int]=[]
        for num in nums:
            if num not in unique:
                unique.append(num)
        nums[:]=unique
        return len(unique)
    # method 2: using set (order doesnt follow)
    def removeDuplicates2(self, nums:list[int])-> int:
        uniques=set(nums)
        nums[:]=uniques
        return len(uniques)

    # method 3: two pointers:
    def removeDuplicates3(self,nums:list[int])->int:
        unique=1
        for i in range(1,len(nums)):
            if nums[unique-1] != nums[i]:
                nums[unique]=nums[i]
                unique +=1
        return unique
    



        


if __name__ =="__main__":
    obj=RemoveDuplicates()

    nums = [1,1,2,8]
    unique=obj.removeDuplicates3(nums)
    print(f'unique elements: {unique} \nunique values: {nums[:unique]}')

    nums = [0,0,1,1,1,2,2,3,3,4,6,7]
    unique=obj.removeDuplicates3(nums)
    print(f'unique elements: {unique} \nunique values: {nums[:unique]}')