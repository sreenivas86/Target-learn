class MinimumWindowSubstring:
    def minWindow(self,s:str,t:str)-> str:
        if t=="":
            return ""
        countT:dict[str,int]={}
        for c in t:
            countT[c] =1+countT.get(c,0)
        res, resLen=[-1,-1],float('inf')
        for l in range(len(s)):
            countS:dict[str,int]={}
            for r in range(l,len(s)):
                countS[s[r]]=1+countS.get(s[r],0)
                flag =True
                for c in countT:
                    if countT[c]>countS.get(c,0):
                        flag =False
                        break
                if flag and (r-l+1)<resLen:
                    resLen= r-l+1
                    res=[l,r]

        l,r=res
        return s[l:r+1] if resLen != float('inf') else ""
    #method 2: sliding window optimal
    def minWindow2(self,s:str,t:str)->str:
        if t=="":
            return ''
        counT:dict[str,int]={}
        windowT:dict[str,int]={}
        for c in t:
            counT[c] =1+counT.get(c,0)
        have,need=0,len(counT)
        res,resLen=[-1,-1],float('inf')
        l=0
        for r in range(len(s)):
            c=s[r]
            windowT[c] =1+windowT.get(c,0)
            if c in counT and windowT[c]==counT[c]:
                have +=1

            while have == need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                windowT[s[l]]-=1
                if s[l] in counT and windowT[s[l]] <counT[s[l]]:
                    have -=1
                l +=1
        l,r=res
        return s[l:r+1] if resLen != float('inf') else ""




if __name__ =="__main__":
    obj=MinimumWindowSubstring()
    s = "OUZODYXAZV"
    t = "XYZ"
    print(obj.minWindow2(s,t))
    s = "xyz"
    t = "xyz"
    print(obj.minWindow2(s,t))
    s = "x"
    t = "xy"
    print(obj.minWindow2(s,t))