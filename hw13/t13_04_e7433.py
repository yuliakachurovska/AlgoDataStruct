def convert_to_base(A: int, P: int):
    if A == 0:
        return "0"
    
    result = []
    while A > 0:
        rem = A % P
        if rem < 10:
            result.insert(0, str(rem)) 
        else:
            result.insert(0, f"[{rem}]")
        A //= P
    return ''.join(result)

if __name__ == "__main__":
    A = int(input())
    P = int(input())
    print(convert_to_base(A, P))