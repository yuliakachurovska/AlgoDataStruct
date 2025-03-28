OPERATORS = {"+": 1, "-": 1, "*": 2, "/": 2}

def convert_prefix_to_infix(expr: str) -> str:
    stack = []
    
    for token in reversed(expr):
        if token in OPERATORS:
            left, left_prio = stack.pop()
            right, right_prio = stack.pop()
            
            if left_prio < OPERATORS[token]:
                left = f"({left})"
            
            if right_prio < OPERATORS[token] or (right_prio == OPERATORS[token] and len(right) > 3):
                right = f"({right})"
            
            new_expr = f"{left}{token}{right}"
            stack.append((new_expr, OPERATORS[token]))
        else:
            stack.append((token, float('inf')))
    
    return stack.pop()[0]

if __name__ == "__main__":
    s = input().strip()
    print(convert_prefix_to_infix(s))