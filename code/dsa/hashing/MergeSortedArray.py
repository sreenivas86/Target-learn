class MergeSortedArray:
    # method 1: sorted
    def mergeSortedArray(self,nums1:list[int],m:int,nums2:list[int], n:int)-> None:
        
        if m==0 and n>1: 
            nums1[:] =nums2
        if m>1 and n==0:
            pa

if __name__ and "__main__":
    obj = MergeSortedArray()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(f'merged array{obj.mergeSortedArray(nums1,m,nums2,n)}')
    nums1 = [1]
    m = 1
    nums2:list[int] = []
    n = 0
    print(f'merged array{obj.mergeSortedArray(nums1,m,nums2,n)}')
    nums1:list[int] = []
    n = 0
    nums2 = [1]
    m = 1
    print(f'merged array{obj.mergeSortedArray(nums1,m,nums2,n)}')