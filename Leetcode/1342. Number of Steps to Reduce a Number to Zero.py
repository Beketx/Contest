def numberOfSteps(num):
    sum=0
    if (num%2!=0) and (num!=0):
	    num=num-1
	    sum+=1
	print(num)
    while num%2==0:
        sum+=1
        num=num/2
        if num==0:
            break
    sum=sum-1
    return sum


print(numberOfSteps(14))