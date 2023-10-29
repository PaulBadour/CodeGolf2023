# DOESNT WORK
import sys
for i in sys.argv[1:]:
    i=list(map(int, i.split(' ')))
    x=i[2]if (i[0]>i[4]and i[0]+i[2]<i[4]+i[6]) else i[6]if(i[0]<i[4]and i[0]+i[2]>i[4]+i[6])else min(abs(i[0]-i[4]+i[6]),abs(i[0]+i[2]-i[4]))
    y=i[3]if (i[1]>i[5]and i[1]+i[3]<i[5]+i[7]) else i[7]if(i[1]<i[5]and i[1]+i[3]>i[5]+i[7])else min(abs(i[1]-i[5]+i[7]),abs(i[1]+i[3]-i[5]))
    print(x*y)