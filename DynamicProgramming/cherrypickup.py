


def maximumCoin(mat, n, m):
    def solve(r,c1,c2):
        if(c1<0 or c2<0 or c1>=m or c2>=m):
            return -1e9
        if(r==n-1):
            if c1==c2:
                return mat[r][c1]
            else:
                return mat[r][c1]+mat[r][c2] 
        else:
            maxi=-1e9
            direction=[-1,0,1]
            for j1 in direction:
                for j2 in direction:
                    if j1==j2:
                        ans=mat[r][c1]+solve(r+1,c1+j1,c2+j2)
                    else:
                        ans=mat[r][c1]+mat[r][c2]+solve(r+1,c1+j1,c2+j2)
                    maxi=max(maxi,ans)

        return maxi
    return solve(0,0,m-1)


mat=[
[0, 2, 4, 1],
[4 ,8, 3, 7],
[2 ,3, 6 ,2],
[9 ,7 ,8 ,3],
[1, 5 ,9, 4]
]

print(maximumCoin(mat,5,4))
