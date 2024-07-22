def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                # Use integer division that truncates toward zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]

if __name__ == "__main__":
    
    token=input().split()
    #print("Input:", token)
    print("Output:", evalRPN(token)) 