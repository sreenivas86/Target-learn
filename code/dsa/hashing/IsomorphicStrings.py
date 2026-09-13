
class IsomorphicStrings:
    # method 1: Hash map two pass
    def isIsomorphic1(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        res:dict[str,str]=dict()
        for i in range(len(s)):
            if s[i] in res and res[s[i]] != t[i]:
                return False
            res[s[i]] = t[i]
            
        return True
    
    # mehtod 2: Two hasmaps one pass
    def isIsomorphic2(self,s:str,t:str) -> bool:
        if len(s) != len(t):
            return False
        dictS,dictT={},{}
        for i in range(len(s)):
            if (s[i] in dictS and dictS[s[i]] != t[i]) or (t[i] in dictT and dictT[t[i]] != s[i]):
                return False
            dictS[s[i]]= t[i]
            dictT[t[i]] =s[i]
        return True
    
if __name__ =='__main__':
    obj=IsomorphicStrings()
    s = "egg"
    t = "add"
    print(obj.isIsomorphic2(s,t))
    
    # test case 2
    s = "f11"
    t = "b23"
    print(obj.isIsomorphic2(s,t))
    # test case 3
    s = "paper"
    t = "title"
    print(obj.isIsomorphic2(s,t))


        