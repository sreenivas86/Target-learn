class HappyNumber:
    # helper function
    def __sum_of_square(self, n:int)-> int:
        ans=0
        while n >0:
            digit= n%10
            ans +=(digit**2)
            n =int(n/10)
            
        return ans
    
    # method 1: using hash set
    def is_happy_num(self,n:int)-> bool:
        seen:set[int]=set()
        while n !=1 and n not in seen:
            seen.add(n)
            n=self.__sum_of_square(n)
        
        return n==1
    
    # method 2: using fast and slow pointers
    def is_happy_num2(self, n:int)-> bool:
        slow =n
        fast= self.__sum_of_square(n)
        
        while slow !=fast:
            fast=self.__sum_of_square(fast)
            fast=self.__sum_of_square(fast)
            slow=self.__sum_of_square(slow)
        return slow ==1
    
    # method 3: using fast and slow pointers II
    def is_happy_num3(self,n:int)->bool:
        slow =n
        fast =self.__sum_of_square(n)
        l=p=1
        while slow != fast:
            if l==p:
                p*=2
                l=0
                slow = self.__sum_of_square(slow)
            l+=1
            fast=self.__sum_of_square(fast)
        return slow ==1
        
        
    
if __name__ == "__main__":
    obj=HappyNumber()
    # print(obj.sum_of_square(162))
    n=100
    print(obj.is_happy_num3(n))
    n=162
    print(obj.is_happy_num3(n))
    n=101
    print(obj.is_happy_num3(n))
    n=10000
    print(obj.is_happy_num3(n))
    n=8
    print(obj.is_happy_num3(n))