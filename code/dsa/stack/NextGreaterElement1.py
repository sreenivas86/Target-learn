class NextGreaterElement:

    # brute force
    def nextGreater(self,nums1:list[int],nums2:list[int])-> list[int]:
        n=len(nums2)
        res:list[int]=[]
        for num in nums1:
            nextG=-1
            for i in range(n-1,-1,-1):
                if num<nums2[i]:
                    nextG=i
                elif num == nums2[i]:
                    break
            res.append(nextG)
            
        
        return res

    # method 2: stack
    def nextGreater1(self,nums1:list[int],nums2:list[int])->list[int]:
        nmap:dict[int,int]={}
        for i,num in enumerate(nums1):
            nmap[num]=i
        res =[-1]*len(nums1)
        stack:list[int]=[]
        for i in range(len(nums2)-1,-1,-1):
            cur=nums2[i]
            while stack and cur> nums2[stack[-1]]:
                stack.pop()
            if stack and cur in nmap:
                idx=nmap[cur]
                res[idx]=stack[-1]
                
            stack.append(i)

        return res

if __name__ =='__main__':
    obj =NextGreaterElement()

    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(obj.nextGreater1(nums1,nums2))
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    print(obj.nextGreater1(nums1,nums2))