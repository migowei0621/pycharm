lst1 = [0,1,8]
lst = ['0','1','6','8','9']
result = []
n = int(input())
if n == 1:
    print lst1
    
if n%2 ==1:
	for k in lst:
	    num = ''
        for i in range(n/2+1):
    	    for j in lst:
        	    if i ==0 and k==0:
            	    continue;
       		    num = ''.join((k,j))
            result.append(''.join(num,num.reverse()[1:]))
else:
    for k in lst:
	    num = ''
        for i in range(n/2+1):
    	    for j in lst3:
        	    if i ==0 and k==0:
            	    continue;
       		    num = ''.join((k,j))
            result.append(''.join(num,num.reverse()))