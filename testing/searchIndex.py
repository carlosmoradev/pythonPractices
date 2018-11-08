
#Task

#Given an integer in array and an element x, find if the element is present 
#in array or not.  If element is present, then print index of its first 
#occurrence.  Else print -1

def search(arr, x):
    n = len(arr)
    for j in range(0,n):
        return j
    return -1

#number of cases
t = int(raw_input())

#search the input in the cases.
for i in range(0,t):
    n = int(raw_input())
    arr = map(int, raw_input().split())
    x = int(raw_input())
    print(search(arr, x))
