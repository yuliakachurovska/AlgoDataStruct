Mod = 301907

def solve(template):
    n = len(template)
    stack = []
    ways = [0] * (n + 1)
    ways[0] = 1
    
    for i in range(n):
        new_w = [0] * (n + 1)
        for open in range(n):
            if ways[open] == 0:
                continue
            
            if template[i] in "(":
                new_w[open + 1] = (new_w[open + 1] + ways[open]) % Mod
                stack.append('(')
            
            if template[i] in ")" and open > 0:
                new_w[open - 1] = (new_w[open - 1] + ways[open]) % Mod
                if stack and stack[-1] == '(':
                    stack.pop()
            
            if template[i] == "?":
                new_w[open + 1] = (new_w[open + 1] + ways[open]) % Mod
                if open > 0:
                    new_w[open - 1] = (new_w[open - 1] + ways[open]) % Mod
        
        ways = new_w
    
    return ways[0]

temp = input().strip()
print(solve(temp))