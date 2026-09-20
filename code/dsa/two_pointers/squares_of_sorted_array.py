class SquaresOfSortedaArray:

    # method1: sorting
    def squaresOfSortedArr1(self,nums:list[int])->list[int]:
        for i in range(len(nums)):
            nums[i] **=2
        nums.sort()
        return nums
    # method 2: two pointers with reverse functinality (find high two low)
    def squaresOfSortedArr2(self,nums:list[int])->list[int]:
        result:list[int]=[]
        l,r=0,len(nums)
        while l<r:
            if nums[l]**2 > nums[r-1]**2:
                result.append(nums[l]**2)
                l +=1
            else:
                result.append(nums[r-1]**2)
                r -=1
        
        return result[::-1]
    # method 3: Two pointes without reverse functionality
    def squaresOfSortedArr3(self,nums:list[int])->list[int]:
        n=len(nums)
        result=[0]*n
        l,r=0,n
        r_index=n-1
        while l<r:
            if nums[l]**2 > nums[r-1]**2:
                result[r_index]=nums[l]**2
                l +=1
                r_index -=1
            else:
                result[r_index]= nums[r-1]**2
                r_index -=1
                r -=1
        return result

    


if __name__ == '__main__':
    obj=SquaresOfSortedaArray()
    nums = [-4,-1,0,3,10]
    print(obj.squaresOfSortedArr3(nums))

    nums = [-7,-3,2,3,11]
    print(obj.squaresOfSortedArr3(nums))