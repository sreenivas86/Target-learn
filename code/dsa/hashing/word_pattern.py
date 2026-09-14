class WordPattern:

    # method1 two hash maps
    def word_pattern_1(self,pattern:str, s:str)-> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        map1,map2={},{}
        for c,w in zip(pattern,words):
            if (c in map1 and map1.get(c)!=w) or (w in map2 and map2.get(w)!=c):
                return False
            map1[c]=w
            map2[w]=c

        return True
    # method 2: Two maps and index (optimal)
    def word_pattern_2(self,pattern:str,s:str)->bool:
        words=s.split(" ")
        if len(words)!=len(pattern):
            return False
        
        map1,map2={},{}
        for i,(c,w) in enumerate(zip(pattern,words)):
            if map1.get(c,0)!= map2.get(w,0):
                return False
            map1[c]=i+1
            map2[w]=i+1
        return True
    # method 3: using hashmap and Hash set
    def word_pattern_3(self,pattern:str,s:str)->bool:
        words= s.split(" ")
        if len(words)!= len(pattern):
            return False
        map1,seen={},set()
        for i,(c,w) in enumerate( zip(pattern,words)):
            if c in map1:
                if words[map1[c]] != w:
                    return False
            else:
                if w in seen: 
                    return False
                map1[c]=i
                seen.add(w)
        return True
    # method 4: single hashamp

    def word_pattern_4(self,pattern:str,s:str)->bool:
        words= s.split(" ")
        if len(words)!=len(pattern):
            return False
        map1={}
        for c,w in zip(pattern,words):
            if c in map1 and map1.get(c)!=w:
                return False
            map1[c]=w
        return True
    

if  __name__ == '__main__':
    obj =WordPattern()
    pattern, s  = "abba", "dog cat cat dog"
    print(obj.word_pattern_4(pattern,s))
    pattern,s = "abba", "dog cat cat fish"
    print(obj.word_pattern_4(pattern,s))
    pattern,s = "aaaa",  "dog cat cat dog"
    print(obj.word_pattern_4(pattern,s))