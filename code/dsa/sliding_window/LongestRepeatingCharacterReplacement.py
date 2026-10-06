class LongestRepeatingCharacterReplacement:
    # method 1: Brute force 
    def characterReplacements(self,s:str, k:int)->int:
        res=0
        for i in range(len(s)):
            count:dict[str,int]={}
            maxc=0
            for j in range(i,len(s)):
                count[s[j]]=1+count.get(s[j],0)
                maxc=max(maxc,count[s[j]])
                if (j-i+1)-maxc<=k:
                    res=max(res,j-i+1)
        return res


    # method 2: sliding window 1
    def characterReplacements2(self,s:str,k:int)->int:
        res=0
        charSet=set(s)
        for c in charSet:
            count=l=0
            for r in range(len(s)):
                if s[r]==c:
                    count +=1
                while (r-l+1)-count >k:
                    if s[l] ==c:
                        count -=1
                    l +=1
                res= max(res,r-l+1)


        return res

    # method 3: Sliding window optimal
    def characterReplacements3(self,s:str,k:int)->int:
        count:dict[str,int]={}
        res= l= maxf=0
        for  r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            maxf=max(maxf,count[s[r]])
            while(r-l+1)-maxf > k:
                count[s[l]] -=1
                l +=1
            res=max(res,r-l+1)


        return res

if __name__ =="__main__":
    obj=LongestRepeatingCharacterReplacement()
    s = "XYYX"
    k = 2
    print (f'output: {obj.characterReplacements3(s,k)}')
    s = "AAABABB"
    k = 1
    print (f'output: {obj.characterReplacements3(s,k)}')