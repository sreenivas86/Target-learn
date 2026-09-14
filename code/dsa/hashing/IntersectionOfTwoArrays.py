from collections import defaultdict
class IntersectionOfArrays:
    
    # method 1: two loops
    def intersectionOfArrays1(self,list1:list[int],list2:list[int])->list[int]:
        res:list[int]=[]
        
        for i in list1:
            for j in list2:
                if i==j and i not in res:
                    res.append(i)
                    break
        return res
    
    # using sets and set methods
    def intersectionOfArrays2(self, list1:list[int],list2:list[int])-> list[int]:
        set1,set2= set(list1),set(list2)
        res =set1.intersection(set2)

        return list(res)

    # method 3: using sets and & operator
    def intersectionOfArrays3(self, list1:list[int], list2:list[int])-> list[int]:
        return list(set(list1)&set(list2))
    
    # method 4: using sets and loop
    def intersectionOfArrays4(self,list1:list[int], list2:list[int])->list[int]:
        set1, set2, res = set(list1), set(list2),[]
        for num in set1:
            if num in set2:
                res.append(num)
        return res
    
    # method 5: using hashmap
    def intersectionOfArrays5(self, list1: list[int], list2: list[int]) -> list[int]:
        """Return the unique values shared by both lists using a hashmap."""
        seen = defaultdict(int)
        res= []
        for num in list1:
            seen[num] +=1
        for num in list2:
            if seen[num] >0:
                seen[num]=0
                res.append(num)
        return res
    # method 6: using set and loop

    def intersectionOfArrays6(self, list1:list[int], list2:list[int])-> list[int]:
        seen, res= set(list1),[]
        for num in list2:
            if num in seen:
                res.append(num)
                seen.remove(num)
        return res



        

if __name__ =='__main__':
    obj= IntersectionOfArrays()
    nums1,nums2= [1,2,2,1],[2,2]
    print(obj.intersectionOfArrays6(nums1,nums2))
    
    nums1, nums2  = [4,9,5], [9,4,9,8,4]
    print(obj.intersectionOfArrays6(nums1,nums2))