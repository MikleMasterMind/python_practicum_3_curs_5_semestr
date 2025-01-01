

def solve():
    n = int(input())
    prev = n + 1
    count = 1
    max_seq = 1
    while n != 0:
        if prev <= n:
            count += 1
        else:
            max_seq = max(max_seq, count)
            count = 1
        prev = n
        n = int(input())
    max_seq = max(max_seq, count)
    print(max_seq)
    
solve()
