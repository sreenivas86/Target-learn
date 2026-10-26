class SearchA2DMatrix:
    def search(self, matrix:list[list[int]],target:int)->bool:
        l=0
        r=len(matrix)-1
        row=-1
        while l<=r:
            mid= (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid])-1]:
                row =mid
                break
            elif matrix[mid][0]> target:
                r=mid-1
            else:
                l=mid +1
        if row == -1:
            return False
        l=0
        r= len(matrix[row])-1
        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r= mid -1
            else :
                l=mid +1
        
        return False


if __name__ =='__main__':
    obj=SearchA2DMatrix()
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 10
    print(obj.search(matrix,target))
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 15
    print(obj.search(matrix,target))