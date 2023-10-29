import sys,datetime as d,calendar as c
[print(c.day_name[d.datetime.strptime(i,"%Y-%m-%d").weekday()])for i in sys.argv[1:]]