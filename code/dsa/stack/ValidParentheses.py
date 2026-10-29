class ValidParentheses:
    def validParanthesis(self,s:str)->bool:
        while '()' in s or '{}' in s or '[]'in s:
            s=s.replace('()','')
            s=s.replace('[]','')
            s=s.replace('{}','')
        return s==''

    # method 2: stack
    def validParanthesis2(self,s:str)->bool:
        stack:list[str]=[]
        pattern={
            ')':'(',
            '}':'{',
            ']':'['
            }
        for c in s:
            if c in pattern:
                if stack and stack[-1] == pattern[c]:
                    stack.pop()
                else :
                    return False
            else :
                stack.append(c)
        return  True if not stack else False



        
if __name__ =="__main__":
    obj =ValidParentheses()
    s = "[]"
    print(obj.validParanthesis2(s))
    s = "([{}])"
    print(obj.validParanthesis2(s))
    s = "[(])"
    print(obj.validParanthesis2(s))
