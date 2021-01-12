# Complexity:
# time: O(n^2)
# space: O(n^2)

def knapsack(W,wt,val,n):
    # initialize the table with 0's 
    # dim of table : (n+1)*(W+1)
    t=[[0 for i in range(W+1)]for j in range(n+1)]
    # value of t[i][j]=0 for i=0 or j=0
    # because its not possible to have zero item of some weight
    # or any item with zero weight
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j: # check is remaining weight is less than item
                # if so then t[i][j] contains the max value with including it or excluding it.
                t[i][j]=max((val[i-1]+t[i-1][j-wt[i-1]]),t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[n][W] 

if __name__=='__main__':
    for cases in range(int(input())):
        n = int(input()) #n: size of lists
        W = int(input())  #W: capacity of knapsack
        val = list(map(int,input().strip().split())) #val: list containing corresponding values
        wt = list(map(int,input().strip().split())) #wt: list containing weights
        print(knapsack(W,wt,val,n))