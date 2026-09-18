class TwoSum2:
    # method 1: brute force method
    def two_sum_II_1(self, numbers:list[int],target:int)-> list[int]:
        
        for i,num in enumerate(numbers):
            for j in range(i+1,len(numbers)):
               if (num+numbers[j])== target:
                   return [i+1,j+1] 
        
        return []
    
    # method 2: two pointes 
    def two_sum_II_2(self, numbers:list[int],target:int)-> list[int]:
        l,r=0,len(numbers)-1
        while l<r:
            low= numbers[l]
            high= numbers[r]
            if (low+high)== target:
                return [l+1,r+1]
            elif (low +high) <target:
                l+=1
            else:
                r-=1
        return []
    # method 3: hash set
    def two_sum_II_3(self, numbers:list[int],target:int)-> list[int]:
        seen:list[int]=[]
        for i,num in enumerate(numbers):
            req=target-num
            if req in seen:
                return [seen.index(req)+1,i+1]
            seen.append(num)
        return []
        



if __name__ =="__main__":
    obj=TwoSum2()
    numbers,target = [2,7,11,15],9
    print(obj.two_sum_II_3(numbers,target))
    numbers,target = [2,3,4],6
    print(obj.two_sum_II_3(numbers,target))
    numbers,target = [-1,0], -1
    print(obj.two_sum_II_3(numbers,target))
    