#높이 = v, 달팽이 = A-B , but 최댓값 -> b = 0
# A = 12시간 , B = 12시간, B>A, 

A, B, V = map(int, input().split())

def snail(A, B, V):
    if (V-B)%(A-B) == 0:
        return (V-B)//(A-B)
    else:
        return (V-B)//(A-B)+1
    
print(snail(A, B, V))