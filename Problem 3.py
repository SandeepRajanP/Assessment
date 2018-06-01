def binary_search(start,end,l,n):
    if start <= end:
        mid = start + (end-start)/2
        if l[mid] == n:
            return mid
        
        if n > l[mid]:
            return binary_search(mid+1,end,l,n)
        else:
            return binary_search(start,mid-1,l,n)      
    else:
        return -1
    
n = int(raw_input())    
l = map(int,raw_input().split())
l = sorted(l)

a = binary_search(0,len(l)-1,l,n)
print a


 
