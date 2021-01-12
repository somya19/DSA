# Complexity:
# time: O(n^2)
# space: O(n^2)

def target_sum(nums, S):    # initialize the table with 0's 
    # dim of table : (n+1)*(s+1)
    n=len(nums)
    total=sum(nums)
    if total<S:
        return 0
    s=(total+S)
    if s%2==1:
        return 0
    s=s//2
    t=[[0 for i in range(s+1)]for j in range(n+1)]
    nums.sort()
    x=nums.count(0)
    #here instead of 1, we store no of ways we can have + or - for 0s 
    for i in range(n+1):
        t[i][0]=2**x
    for i in range(1,n+1):
        for j in range(1,s+1):
            if nums[i-1]<=j:
                t[i][j]=t[i-1][j-nums[i-1]] + t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[n][s]

if __name__=='__main__':
    for cases in range(int(input())):
        l = list(map(int,input().split())) #l: list of elements
        S = int(input())  #S: sum
        print(target_sum(l,S))