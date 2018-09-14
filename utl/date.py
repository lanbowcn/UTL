import datetime
import pandas as pd
#对日期字符进行读取，及变换
a="2003/10/10 16:10:00"
b=datetime.datetime.strptime(a,"%Y/%m/%d %H:%M:%S")
print(b.strftime('%Y-%m'))

#将日期作为index进行排序
data = pd.read_csv('../dataset2/jdt.csv', index_col='commitdate', parse_dates=True).sort_index()

df = pd.read_table('G:/tc/dataset/user_view.txt', sep=",")
