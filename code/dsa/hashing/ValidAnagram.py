class Solution:
    # Bruteforce or sort a string appoch
    
    def isAnagram1(self,s:str,t:str)->bool:
        if len(s)!= len(t):
            return False
        
        return sorted(s) == sorted(t)
    # HashMap or dictinary
    def isAnagram2(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        dictt=dict()
        dicts=dict()
        for i in range(len(s)):
            dicts[s[i]]= 1+dicts.get(s[i],0)
            dictt[t[i]]= 1+dictt.get(t[i],0)
        return dictt==dicts
            
    
    # single HashMap
    def isAnagram3(self, s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        hashmap=dict()
        for i in range(len(s)):
            hashmap[s[i]]= hashmap.get(s[i],0)-1
            hashmap[t[i]]= hashmap.get(t[i],0)+1
        # iterate values 
        for i in hashmap.values():
            if i!=0:
                return False
        return True
    
    
    # using single list with fixed length 26. 
    # it is applicable when both string in lowercase or uppercase
    # ord(char): it use to find unicode of a character
    def isAnagram4(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        count=[0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] +=1
            count[ord(t[i])-ord('a')] -=1
        
        for i in count:
            if i !=0:
                return False
        return True
    
    
        
if __name__== "__main__":
    obj=Solution()
    
    s= 'master'
    t= 'stream'
    print(obj.isAnagram4(s,t))
    