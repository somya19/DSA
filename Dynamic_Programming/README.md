# 0-1 KNAPSACK PROBLEMS #
These problems can be solved using reference of standard 0-1Knapsack problem.<br> 
### 1.[0-1 KnapSack](https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1)<br> ###
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.<br>
### 2.Subset Sum Problem <br> ###
Given an array arr[] of size N, check if there exist any subset with sum S. We can use 0-1 knapsack to solve this as here we need to choose some elements from the arr[] which sum up to S.
### 3.[Equal Sum Partition Problem](https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1)<br> ###
Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same. This question can be solved using Subset Sum Partition. <br>
So if it is possible to have a subset with sum as S/2 then sum of elements left will be s/2. Hence, equal sum partitions. <br>
Else, not possible. Also, it is only possible to have equal sum partition if sum is even.<br>
### 4.[Count Subsets of Given Sum](https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1)<br> ###
Given an array arr[] of integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.This question can be solved using Subset Sum Partition by instead of recording if there exists any subset with sum S, record count by replacing "or" with "+".<br>
### 5.[Target Sum](https://leetcode.com/problems/target-sum/)<br>
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.Find out how many ways to assign symbols to make sum of integers equal to target S.<br>
Let sum of positive nos be s1,<br>
sum of neg nos be s2<br>
So, s1-s2=S and s1+s2=sum(arr)
    => s1=(S+sum(arr))//2<br>
This problem is similar to "Count Subsets of Given Sum" where given sum is s1.  <br>


# LCS #
These problems can be solved using reference of standard lcs problem.<br> 
### 6.[Longest Common Subsequence](https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1)<br>
Given two sequences, find the length of longest subsequence present in both of them. <br>
### 7.[Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)<br>
Given a string s, find the longest palindromic subsequence's length in s.<br>









