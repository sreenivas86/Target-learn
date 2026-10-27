class  CapacityToShip:
    def minCapacity(self,weights:list[int],days:int)->int:
        minCap=max(weights)
        maxCap= sum(weights)
        while minCap <=maxCap:
            ship=1
            total=0
            for num in weights:
                if total +num > minCap:
                    ship +=1
                    total =num
                else:
                    total +=num
            if ship<=days:
                return minCap
            minCap +=1
        return maxCap

    # method 2: Binary search
    def minCapacity2(self,weights:list[int],days:int)->int:

        def minShip(cap:int)->bool:
            ship=1
            total =0
            for w in weights:
                if total +w> cap:
                    ship +=1
                    total =w
                else :
                    total +=w

            return ship<=days

        l=max(weights)
        r=sum(weights)
        
        while l<=r:
            mid =(l+r)//2
            if  minShip(mid):
                r=mid -1
            else:
                l=mid+1
        return l

                


       

if __name__ =='__main__':
    obj = CapacityToShip()
    weights = [2,4,6,1,3,10]
    days = 4
    print(obj.minCapacity2(weights,days))
    weights = [1,2,3,4,5]
    days = 5
    print(obj.minCapacity2(weights,days))