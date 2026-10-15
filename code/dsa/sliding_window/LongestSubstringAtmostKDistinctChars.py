class LongestSubstringAtMostKDistinctChars:
    #method 1: brute force
    def longestSubstring(self,s:str,k:int)->int:
        res =-1
        for i in range(len(s)):
            freq:dict[str,int]={}
            for j in range(i,len(s)):
                c=s[j]
                freq[c]=freq.get(c,0)
                if len(freq)>k:
                    break
                if len(freq) == k:
                    res =max(res,j-i+1)
        return res
    # method 2: dynamic sliding window wiht hash map
    def longestSubstring2(self,s:str,k:int)->int:
        res =-1
        left =0
        freq:dict[str,int]={}
        for right in range(len(s)):
            freq[s[right]]=1+freq.get(s[right],0)
            while len(freq)>k:
                freq[s[left]] -=1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left +=1
            if len(freq) == k:
                res = max(res,right -left+1)
        return res
    # method 3: dynamic sliding window with hash array
    def longestSubstring3(self,s:str,k:int)->int:
        res,left=-1,0
        freq=[0]*26
        cnt=0
        for right,char in enumerate(s):
            freq[ord(char)-ord('a')] +=1
            if freq[ord(char)-ord('a')] ==1:
                cnt +=1
            while cnt >k:
                freq[ord(s[left])-ord('a')] -=1
                if freq[ord(s[left])-ord('a')] ==0:
                    cnt -=1
                left +=1
            if cnt == k:
                res =max(res,right-left+1)
        return res
                



if __name__ =="__main__":
    obj =LongestSubstringAtMostKDistinctChars()
    s = "aabacbebebe"
    k = 3
    print(obj.longestSubstring3(s,k))
    s = "aaaa"
    k = 2
    print(obj.longestSubstring3(s,k))
    s = "aabaaab"
    k = 2   
    print(obj.longestSubstring3(s,k))    
