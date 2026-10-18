class FruitsIntoBasket:
    # method 1: Brute Force
    def fruitsIntoBasket(self,fruits:list[int])->int:
        res =0
        for i in range(len(fruits)):
            basket:set[int]=set()
            for j in range(i,len(fruits)):
                basket.add(fruits[j])
                if len(basket)>2:
                    break
                res =max(res,j-i+1)
        return res
    # method 2: sliding window with Hash map optimal solution
    def fruitsIntoBasket2(self,fruits:list[int])->int:
        res=0
        basket:dict[int,int]={}
        left=0
        for right in range(len(fruits)):
            fruit=fruits[right]
            basket[fruit] =1+basket.get(fruit,0)
            while len(basket)>2:
                basket[fruits[left]] -=1
                if basket[fruits[left]] ==0:
                    del basket[fruits[left]]
                left +=1
            res =max(res,right-left+1)
        return res


if __name__ =="__main__":
    obj =FruitsIntoBasket()
    fruits= [1,2,1]
    print(obj.fruitsIntoBasket2(fruits))
    fruits=[0,1,2,2]
    print(obj.fruitsIntoBasket2(fruits))
    fruits=[1,2,3,2,2]
    print(obj.fruitsIntoBasket2(fruits))
