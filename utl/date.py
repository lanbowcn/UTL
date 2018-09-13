import datetime
#对日期字符进行读取，及变换
a="2003/10/10 16:10:00"
b=datetime.datetime.strptime(a,"%Y/%m/%d %H:%M:%S")
print(b.strftime('%Y-%m'))