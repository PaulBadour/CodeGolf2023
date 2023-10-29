import sys,copy
b=list(map(list,sys.argv[1].split('\n')))
n=copy.deepcopy(b)
for i,k in enumerate(b):
    for j,l in enumerate(k):
        c=0
        c+=1 if i-1>=0 and b[i-1][j]=='#'else 0
        c+=1 if i+1<32 and b[i+1][j]=='#'else 0
        c+=1 if j-1>=0 and b[i][j-1]=='#'else 0
        c+=1 if j+1<32 and b[i][j+1]=='#'else 0
        c+=1 if i-1>=0 and j-1>=0 and b[i-1][j-1]=='#'else 0
        c+=1 if i-1>=0 and j+1<32 and b[i-1][j+1]=='#'else 0
        c+=1 if i+1<32 and j-1>=0 and b[i+1][j-1]=='#'else 0
        c+=1 if i+1<32 and j+1<32 and b[i+1][j+1]=='#'else 0
        if b[i][j]=='.':
            n[i][j]='#'if c==3 else'.'
        else:
            n[i][j]='#'if 2<=c<=3 else'.'
    print(''.join(n[i]))