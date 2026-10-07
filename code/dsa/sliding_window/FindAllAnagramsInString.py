class FindAllAnagrams:
    #method 1: Brute Force
    def findAllAnagrams(self,s:str,p:str)->list[int]:
        res:list[int]=[]
        p1=sorted(p)
        m=len(s)
        n=len(p)
        for i in range(m-n+1):
            sub=sorted(s[i:i+n])
            if sub==p1:
                res.append(i)


        return res

    # method2: sliding window and hashmap
    def findAllAnagrams2(self,s:str,p:str)->list[int]:
        m,n=len(s),len(p)
        if n>m:
            return []
        res:list[int]=[]
        smap:dict[str,int]={}
        pmap:dict[str,int]={}
        for i in range(n):
            smap[s[i]] = 1+smap.get(s[i],0)
            pmap[p[i]] = 1+pmap.get(p[i],0)
        if smap==pmap:
            res.append(0)
        l=0
        for r in range(n,m):
            smap[s[r]]=1+smap.get(s[r],0)
            smap[s[l]]-=1
            if smap[s[l]]==0:
                del smap[s[l]]
            l+=1
            if smap ==pmap:
                res.append(l)

        return res

    # method 3: sliding window with hashing
    def findAllAnagrams3(self,s:str,p:str)->list[int]:
        m,n=len(s),len(p)
        if n>m:
            return []
        res:list[int]=[]
        scount,pcount=[0]*26,[0]*26
        for i in range(n):
            scount[ord(s[i])-ord('a')] +=1
            pcount[ord(p[i])-ord('a')] +=1
        if scount == pcount:
            res.append(0)
        l =0
        for r in range(n,m):
            scount[ord(s[r])-ord('a')]  +=1
            scount[ord(s[l])-ord('a')]  -=1
            l+=1
            if scount ==pcount:
                res.append(l)
        return res   

    


if __name__ =='__main__':
    obj=FindAllAnagrams()
    s = "cbaebabacd"
    p = "abc"
    print(obj.findAllAnagrams3(s,p))
    s = "abab"
    p = "ab"
    print(obj.findAllAnagrams3(s,p))
        