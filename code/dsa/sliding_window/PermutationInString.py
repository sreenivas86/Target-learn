class PermutationInString:
    #method 1: Brute force
    def permutationInString(self,s1:str,s2:str)->bool:
        s3=sorted(s1)
        for i in range(len(s2)):
            for  j in range(i,len(s2)):
                subStr=s2[i:j]
                subStr=sorted(subStr)
                
                if s3==subStr:
                    return True

        return False
    # method 2: Hash Tables or map 
    def permutationInString2(self,s1:str,s2:str)->bool:

        count1:dict[str,int]={}
        for c in s1:
            count1[c] =1+count1.get(c,0)
        need =len(count1)
        for i in range(len(s2)):
            count2:dict[str,int]={}
            curr=0
            for j in range (i,i+len(s2)):

                count2[s2[j]] =1+count2.get(s2[j],0)
                if count2.get(s2[j],0) >count1.get(s2[j],0):
                    break

                if count2.get(s2[j]) == count1.get(s2[j],0):
                    curr +=1
                if curr ==need:
                    return True
        return False

    #method 3: sliding window
    def permutationInString3(self,s1:str,s2:str)-> bool:
        if len(s1) > len (s2):
            return False
        s1_count, s2_count=[0]*26, [0]*26
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] +=1
            s2_count[ord(s2[i])-ord('a')] +=1
        match =0
        for i in range(26):
            if s1_count[i]==s2_count[i]:
                match +=1
        
        l=0
        for r in range(len(s1),len(s2)):
            if match ==26:
                return True
            index = ord(s2[r])- ord('a')
            s2_count[index] +=1
            if s2_count[index] == s1_count[index]:
                match +=1
            elif s1_count[index]+1 == s2_count[index]:
                match -=1

            index = ord(s2[l])-ord('a')
            s2_count[index] -=1
            if s2_count[index]==s1_count[index]:
                match +=1
            elif s1_count[index]-1 ==s2_count[index]:
                match -=1
            l+=1

            
        return False

if __name__ =="__main__":
    obj = PermutationInString()

    s1 = "abc"
    s2 = "lecabee"
    print(obj.permutationInString3(s1,s2))


    "abc"
    s2 = "lecaabee"
    print(obj.permutationInString3(s1,s2))