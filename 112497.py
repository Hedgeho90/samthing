a = input()
a = a.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('/', ' / ')

def f(a):
    postfix = []
    stack = []
    p= {'+': 1, '-': 1, '*': 2, '/': 2}

    for i in a.split():
        if i.isdigit():
            postfix.append(i)
        elif i in ('+', '-', '*', '/'):
            while stack and stack[-1] in ('+', '-', '*', '/') and p[stack[-1]] >= p[i]:
                postfix.append(stack.pop())
            stack.append(i)
    while stack:
        postfix.append(stack.pop())
    return ' '.join(postfix)
print(f(a))