from collections import Counter
class RansomNote:
    # method 1 using list
    def ransomNote1(self, ransom:str,magazine:str)-> bool:
        n,m=len(ransom),len(magazine)
        
        if n>m:
            return False
        magazinel=list(magazine)
        for i in ransom:
            if i not in magazinel:
                return False
            magazinel.remove(i)
        return True
    
    # method 2 using hashmap or dictionary
    def ransomNote2(self,ransom:str,magazine:str)->bool:
        if len(ransom)> len(magazine):
            return False
        dictR:dict[str,int]=dict()
        dictM:dict[str,int]=dict()
        for c in magazine:
            dictM[c] = dictM.get(c,0)+1
        for c in ransom:
            dictR[c]=dictR.get(c,0)+1
        # comparison
        for c in ransom:
            if dictR.get(c,0)>dictM.get(c,0):
                return False
        return True
    
    # method 3 Counter() from collections
    def ransomNote3(self, ransom:str,magazine:str)->bool:
        if len(ransom)> len(magazine):
            return False
        dictR=Counter(ransom)
        dictM=Counter(magazine)
        for c in ransom:
            if dictR.get(c,0)> dictM.get(c,0):
                return False

        return True
    # method 4 single dictionary
    def ransomNote4(self,ransom:str,magazine:str)->bool:

        if len(ransom)> len(magazine):
            return False
        dictM=Counter(magazine)
        for c in ransom:
            dictM[c]= dictM.get(c,0)-1
            if dictM.get(c,0)<0:
                return False
        return True
    # method 5 using hashing method (note: those both string are in same case)
    def ransomNote5(self, ransom:str,magazine:str)->bool:
        if len(ransom)> len(magazine):
            return False
        hash=[0]*26
        for c in magazine:
            hash[ord(c)-ord('a')] +=1
        for c in ransom:
            hash[ord(c)-ord('a')] -=1
            if hash[ord(c)-ord('a')]<0:
                return False
        return True


if __name__ == '__main__':
    obj= RansomNote()
    
    # test case 1
    ransomNote = "aa"
    magazine = "aab"
    print(obj.ransomNote5(ransomNote,magazine))
    # test case 2
    ransomNote = "aa"
    magazine = "ab"
    print(obj.ransomNote5(ransomNote,magazine))
    
    