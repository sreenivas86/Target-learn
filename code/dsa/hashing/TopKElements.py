from ast import List
import heapq

class TopKElements:

    # mehtod 1: sorting

    def topKElements(self, nums:list[int],k:int)->list[int]:
        count:dict[int,int]={}
        for num in nums:
            count[num]=1+count.get(num,0)
        arr:list[list[int]]=[]
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
        res:list[int]=[]
        for _ in range(k):
            res.append((arr.pop())[1])
        return res
    # method2: Using heapq in python
    def topKElements2(self,nums:list[int],k:int)->list[int]:
        count:dict[int,int]={}
        for num in nums:
            count[num]=1+count.get(num,0)
        heap:list[list[int]]=[]
        for key in count.keys():
            heapq.heappush(heap,[count[key],key])
            if len(heap)>2:
                heapq.heappop(heap)
        res:list[int]=[0]*k
        
        for i in range(k,0,-1):
            res[i-1]=heapq.heappop(heap)[1]
            #res.append(heapq.heappop(heap)[1])
        return res
    # method 3: bucket sort
    def topKElements3(self,nums:list[int],k:int)->list[int]:
        count:dict[int,int]={}
        bucket:list[list[int]]=[[] for _ in range(len(nums)+1)]
        for num in nums:
            count[num]=1+count.get(num,0)
        for num,cnt in count.items():
            bucket[cnt].append(num)
        res:list[int]=[]
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)>2:
                    res.pop()
        return res
if __name__ =="__main__":
    obj=TopKElements()
    nums = [1,2,2,3,3,3]
    k = 2
    print(obj.topKElements3(nums,k))
    nums = [7,7]
    k = 1
    print(obj.topKElements3(nums,k))