import csv
import numpy as np
from operator import itemgetter

def del_cvs_col(fname, newfname, idxs, delimiter=' '):
    with open(fname) as csvin, open(newfname, 'w',newline='') as csvout:
        reader = csv.reader(csvin, delimiter=delimiter)
        writer = csv.writer(csvout, delimiter=delimiter)
        for row in reader:
            for item in row:
                for i in item:
                    print(i)
        # rows = (tuple(item for idx, item in enumerate(row) if idx not in idxs) for row in reader)
        # writer.writerows(rows)

# del_cvs_col('ant-1.7.csv', 'b.csv', [2])









# ++++++++++++++++++++++++++++++++++++++++++++++++++++






input_file = open("ant-1.7.csv")
output_file = open("b.csv","w",newline='')
table = []
header = input_file.readline() #读取并弹出第一行
header = header.strip('\n')
header = header.split(',')
header = header[3:]
header.insert(0,'fileID')
header.insert(-1,'defect')
print(header)

i = 0
for line in input_file:
    line = line.strip('\n')
    col = line.split(',')
    col = col[3:]
    if col[-1]!='0':
        col.insert(-1,'1')
    else:
        col.insert(-1,'0')
    col.insert(0,i)
    i=i+1
    print(col)
    table.append(col)

# output_file.write(header+'\t')
writer = csv.writer(output_file)
writer.writerow(header)
for row in table:
    row = [str(x) for x in row]
    # output_file.write("\t".join(row)+'\n')
    writer.writerow(row)

input_file.close()
output_file.close()




