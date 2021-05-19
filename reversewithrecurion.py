arr=[1,2,3,4,5]
l=0
n=len(arr)
def fun(arr,l):
    if(l==n//2): # we can stop the loop when we reaches the middle of the arr
        return arr
    else:
        arr[l],arr[n-1-l]=arr[n-1-l],arr[l] #l=0,n-1-0->5-1-0->4
                                            #we are checking replacing 1st element with the last element using only one variable
        
        return fun(arr,l+1)


res=fun(arr,l)
print(res)
