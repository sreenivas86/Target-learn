
class ValidPalindrom:
    # method 1: reverse  a string 
    def is_valid_palindrome_1(self,s:str)-> bool:
        newStr= ""
        for i in s:
            if  i.isalnum():
                newStr+=i.lower()
        return newStr == newStr[::-1]
    
    # method 2: two pointers
    def is_valid_palindrome_2(self,s:str)->bool:
        first,last=0,len(s)-1
        while first<last:
            
            while first<last and   not(s[first].isalnum()):
                first +=1
            while last>first and  not(s[last].isalnum()):
                last -=1
            if s[first].lower() !=s[last].lower():
                return False
            first,last= first+1,last-1
        return True




if __name__ =='__main__':
    obj=ValidPalindrom()
    
    s = "A man, a plan, a canal: Panama" #True
    print(obj.is_valid_palindrome_2(s))
    s = "race a car" # false
    print(obj.is_valid_palindrome_2(s))
    s = " " # true
    print(obj.is_valid_palindrome_2(s))