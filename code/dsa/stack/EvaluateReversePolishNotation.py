class EvaluateReversePolishNotation:
    def evalNotation(self,tokens:list[str])->int:

        stack:list[int] =[]
        for c in tokens:
            if c in '+-*/':
                if c == '+':
                    stack.append(stack.pop()+stack.pop())
                elif c == '-':
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b-a)
                elif c == '*':
                    stack.append(stack.pop()*stack.pop())
                elif c== '/':
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(b/a))
            else :
                stack.append(int(c))
        return stack[0]


if  __name__ == "__main__":
    obj= EvaluateReversePolishNotation()
    tokens = ["1","2","+","3","*","4","-"]
    print(f'output : {obj.evalNotation(tokens)}')
    tokens = ["2","1","+","3","*"]
    print(f'output : {obj.evalNotation(tokens)}')
    tokens =["4","13","5","/","+"]
    print(f'output : {obj.evalNotation(tokens)}')
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(f'output : {obj.evalNotation(tokens)}')