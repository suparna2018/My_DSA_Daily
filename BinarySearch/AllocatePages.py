def isPossible(val,n,m,arr):
    currSum=0
    student=1
    for i in range(n):
        if arr[i]>val:
            return False
       
        if currSum+arr[i]>val:
            currSum=arr[i]
            student+=1

            if student>m:
                return False
        else:
             currSum+=arr[i]
    return True
            

def findPages(arr,n,m):
    lo,hi=min(arr),sum(arr)
    res=1e9
    while(lo<=hi):
        mid=(lo+hi)//2
        if(isPossible(mid,n,m,arr)):
            res=mid
            hi=mid-1
        else:
            lo=mid+1
    return res


# Number of pages in books
arr = [12, 34, 67, 90]
n = len(arr)
m = 2   # No. of students

print("Minimum number of pages = ",
      findPages(arr, n, m))