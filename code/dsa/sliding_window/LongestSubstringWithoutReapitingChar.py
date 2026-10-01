class LongestSubstring:
    # method 1: bruteforce
    def longestSubstring1(self,s:str)->int:
        res=0
        for i in range(len(s)):
            charSet:set[str]=set()
            for j in range(i,len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res=max(res,len(charSet))

        return res
    # method 2: sliding window with hash set best approch
    def longestSubstring2(self,s:str)->int:
        res=0
        charSet:set[str]=set()
        l=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res
    #method 3: sliding window with hashmap(optimal)
    def longestSubstring3(self,s:str)->int:
        res=0
        mp:dict[str,int]={}
        l=0
        for r in range(len(s)):
            if s[r]in mp:
                l=max(mp.get(s[r],0)+1,l)
            mp[s[r]]=r
            res=max(res,r-l+1)
        return res


if __name__ == "__main__":
    obj=LongestSubstring()
    s = "zxyzxyz"
    print(f'len of longest substring without repeating charecters {obj.longestSubstring3(s)}')
    s = "xxxx"
    print(f'len of longest substring without repeating charecters {obj.longestSubstring3(s)}')