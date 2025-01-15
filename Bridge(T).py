def bridge(T):
    from math import inf
    N=len(T)
    min_cost=inf
    cur_cost=0
    for row in range(N):
        for col in range(N):
            if T[row][col]>0:
                x=1
                while T[row][col+x]==T[row][col] and col+x<N:
                    x+=1
                    continue
                while T[row][col+x]<0 and col+x<N:
                    cur_cost-=T[row][col+x]
                    x+=1
                if T[row][col+x]>0 and T[row][col+x]!=T[row][col]:
                    min_cost=min(min_cost, cur_cost)
                cur_cost=0
                y=1
                while row+y<N and T[row+y][col]==T[row][col]:
                    y+=1
                    continue
                while row+y<N and T[row+y][col]<0:
                    cur_cost-=T[row+y][col]
                    y+=1
                if row+y<N and T[row+y][col]>0 and T[row+y][col]!=T[row][col]:
                    min_cost=min(min_cost, cur_cost)
                cur_cost=0
                break
    return min_cost

tablica = [
    [-2,-1,-1,-1,-1,-2,-1],
    [-1, 1, 1, 1,-3,-1,-1],
    [-1, 1,-1,-2,-2, 3, 3],
    [-1,-1, 2, 2,-7, 3, 3],
    [-1,-2, 2,-3,-1,-1, 3]
]
print(bridge(tablica))
