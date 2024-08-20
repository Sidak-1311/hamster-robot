i=0
def Reduce(N):
    global i
    nums=[]
    if N==1:
         return 0
    else:
        if N%3==0:
            nums.append(N/3)
        elif ((N-1)%3==0):
            nums.append(N-1)
        
        elif ((N%2)==0):
            nums.append(N/2)
        else:
            nums.append(N-1) 
    i=i+1
    nums.sort()
    Reduce(nums[0])


Reduce(11)
print(str(i) + " steps to 1")