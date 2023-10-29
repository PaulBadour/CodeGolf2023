l=[0,1]
for i in range(29):l+=[sum(l[-2:])]
for i in l:print(i)