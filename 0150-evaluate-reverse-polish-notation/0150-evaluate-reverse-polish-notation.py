class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==0:
            return 0
        stack=[]
        res=0
        for t in tokens:
            if t in "+-*/":
                b=int(stack.pop())
                a=int(stack.pop())
                if t=='+':
                    res=a+b
                elif t=='-':
                    res=a-b
                elif t=='*':
                    res=a*b
                else:
                    res=int(a/b)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]
                
                    
                