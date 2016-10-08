def reverse(x):
    old_x = x
    if (x<0):
        x = x * -1
    array = []

    for i in range(1,len(str(x))+1):
        array.append(x%10)
        x = (x - x%10)/10
    fresult = int(''.join(str(k) for k in array))
    if (old_x < 0):
        array.insert(0,'-')
    result = int(''.join(str(j) for j in array))
    if not(fresult>>31):
    	print result
    	print type(result)
    else:
    	print 0

reverse(156384741)

