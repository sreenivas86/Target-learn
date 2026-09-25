class MergeSortedArray:
    # method 1: sorted
    def mergeSortedArray(self,nums1:list[int],m:int,nums2:list[int], n:int)-> None:
        #nums1[m:]=nums2[:n]
        
        for i in range(n):
            
            if m==1:
                m=0
            nums1[m+i]= nums2[i]
        nums1.sort()
        
        
    # method 2: Three pointer with extra space
    def mergeSortedArray2(self,nums1:list[int],m:int,nums2:list[int],n:int)->None:
        l,r,index=0,0,0
        if m==1 and n==1:
             nums1[index]=nums2[0]
             index +=1
             return None
        nums1_copy=nums1[:m]
        
        while index<m+n :
            if r>=n or(l<m and nums1_copy[l]<nums2[r]):
                nums1[index] =nums1_copy[l]
                l+=1
            else:
                nums1[index] = nums2[r]
                r+=1
            index +=1
    # method 2: Three pointer I without extra space
    def mergeSortedArray3(self,nums1:list[int],m:int,nums2:list[int],n:int)->None:
        index =m+n-1
        if m==1 and n==1:
            nums1[0]=nums2[0]
            return None
        while m>0 and n>0:
            if nums1[m-1] >nums2[n-1]:
                nums1[index]=nums1[m-1]
                m=m-1
            else:
                nums1[index]= nums2[n-1]
                n=n-1
            index -=1
        while n>0:
            nums1[index]=nums2[n-1]
            index-=1
            n-=1
            
    # method 4: three pointer II with out space
    def mergeSortedArray4(self,nums1:list[int], m:int,nums2:list[int],n:int)->None:
        if m==1 and n==1:
            nums1[0]=nums2[0]
            return None
        last=m+n-1
        l,r=m-1,n-1
        while l>=0 and r>= 0:
            if nums1[l] >nums2[r]:
                nums1[last]=nums1[l]
                l-=1
            else:
                nums1[last]=nums2[r]
                r -=1
            last -=1
        while r>=0:
            nums1[last] = nums2[r]
            r-=1
        
        

if __name__ and "__main__":
    obj = MergeSortedArray()
    nums1 = [1,2,3,7,0,0,0]
    m = 4
    nums2 = [2,5,6]
    n = 3
    obj.mergeSortedArray4(nums1,m,nums2,n)
    print(f'merged array{nums1}')
    nums1 = [1]
    m = 1
    nums2:list[int] = []
    n = 0
    obj.mergeSortedArray4(nums1,m,nums2,n)
    print(f'merged array{nums1}')
    nums1:list[int] = [0]
    m = 1
    nums2 = [1]
    n = 1
    obj.mergeSortedArray4(nums1,m,nums2,n)
    print(f'merged array{nums1}')