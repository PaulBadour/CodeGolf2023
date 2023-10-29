for l in range(9):
    [print((' '*(10-i))+''.join([str(j)for j in range(1,i+1)])+''.join([str(j)for j in range(i-1,0,-1)])+(' '*(10-i)))for i in[j for j in range(1,l+2)]+[k for k in range(l,0,-1)]]
    print('')