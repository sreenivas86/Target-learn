class GroupAnagram:
    
    # method 1: to use sorting.
    def group_anagram_1(self, strs:list[str])->list[list[str]]:
        anagrams:dict[str,list[str]]={}
        for w in strs:
            sort_w="".join(sorted(w))
            anagrams.setdefault(sort_w,[]).append(w)
        return list(anagrams.values())
    
    # method 2: to use hashing
    def group_anagram_2(self,strs:list[str])-> list[list[str]]:
        anagram:dict[tuple[int,...],list[str]]={}
        for w in strs:
            letters:list[int]=[0]*26
            for i in w:
                letters[ord(i)-ord('a')]+=1
            anagram.setdefault(tuple(letters),[]).append(w)
        return list(anagram.values())
    
    
if __name__ == '__main__':
    obj= GroupAnagram()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(obj.group_anagram_2(strs))