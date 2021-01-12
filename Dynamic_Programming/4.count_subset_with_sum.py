# Complexity:
# time: O(n^2)
# space: O(n^2)

def count_subset(arr,s,n):
    # initialize the table with 0's 
    # dim of table : (n+1)*(s+1)
    t=[[0 for i in range(s+1)]for j in range(n+1)]
    
    # initialize the 0th row to 1, as it is possible to have sum=0 (empty subset)  
    for i in range(n+1):
        t[i][0]=1

    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j]=t[i-1][j]           
    return t[n][s] 

if __name__=='__main__':
    for cases in range(int(input())):
        n = int(input()) #n: size of list
        l = list(map(int,input().split())) #l: list of elements
        S = int(input())  #S: sum
        print(count_subset(l,S,n))