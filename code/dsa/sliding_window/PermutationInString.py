class PermutationInString:
    #method 1: Brute force
    def permutatioInString(self,s1:str,s2:str)->bool:
        s3=sorted(s1)
        for i in range(len(s2)):
            for  j in range(i,len(s2)):
                subStr=s2[i:j]
                subStr=sorted(subStr)
                
                if s3==subStr:
                    return True

        return False



if __name__ =="__main__":
    obj = PermutationInString()

    s1 = "abc"
    s2 = "lecabee"
    print(obj.permutatioInString(s1,s2))


    "abc"
    s2 = "lecaabee"
    print(obj.permutatioInString(s1,s2))