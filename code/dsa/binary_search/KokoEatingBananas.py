import math
class KokoEatingBananas:
    def minEatingSpeed(self,piles:list[int],h:int)-> int:
        l=1
        r=max(piles)
        minSpeed=r
        while l <r:
            speed=(l+r)//2
            total =0
            for num in piles:
                total += math.ceil(num/speed)
            if total <=h:
                minSpeed=min(minSpeed,speed)
                r=speed-1
            else:
                l=speed+1

        return minSpeed

if __name__ =='__main__':
    obj=KokoEatingBananas()
    piles = [1,4,3,2]
    h = 9
    print(obj.minEatingSpeed(piles,h))
    piles = [25,10,23,4]
    h = 4
    print(obj.minEatingSpeed(piles,h))