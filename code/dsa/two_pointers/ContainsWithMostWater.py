class ContainerWithMostWater:
    #method 1: bruteforce
    def containerWithMostWater1(self,height:list[int])->int:
        
        res=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                current= min(height[i],height[j]) * (j-i)
                res=max(res,current)
                
        return res  
    
    def containerWithMostWater2(self,height:list[int])->int:
        res =0
        l=0
        r=len(height)-1
        
        while l<r:
            current=min(height[l],height[r]) * (r-l)
            res= max(res,current)
            if height[l]> height[r]:
                r=r-1
            else:
                l+=1
        
        return res  

if __name__ =='__main__':
    obj = ContainerWithMostWater()
    height=[1,8,6,2,5,4,8,3,7]
    print(f'area of bigger container {obj.containerWithMostWater2(height)}')
    height = [1,1]
    print(f'area of bigger container {obj.containerWithMostWater2(height)}')
    height = [2,2,2]
    print(f'area of bigger container {obj.containerWithMostWater2(height)}')
    height = [1,7,2,5,4,7,3,6]
    print(f'area of bigger container {obj.containerWithMostWater2(height)}')