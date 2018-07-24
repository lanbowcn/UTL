import xlrd
import xlwt
from datetime import date, datetime


def read_excel():
    # 打开文件
    data = xlrd.open_workbook(r'grd-5.xlsx')
    # 获取所有sheet
    table = data.sheets()[0]

    #找到第一个同学的成绩
    for n in range(int(table.nrows/4)):
        #找到名称行并读取
        keyrow = n*4+2#名称行
        valrow = keyrow+1#值行
        first_row_values = table.row_values(n*4+1)

        #成绩
        print('    尊敬的家长您好！寒假已至，您的孩子' + table.cell_value(valrow,1)+'在重庆大学顺利平安地度过了大三第一个学期，现将他的学习成绩通知如下:',end='')
        for i in range(2,len(first_row_values)):
            ctype = table.cell(valrow, i).ctype
            keycell = table.cell_value(keyrow,i)
            valcell = table.cell_value(valrow, i)
            if ctype == 2 and valcell % 1 == 0.0:
                valcell = int(valcell)
            if keycell != '':
                print(str(keycell)+':'+str(valcell)+',',end='')
        print(' ')
        print('    我校暑假时间为2018年7月16日—8月31日，学生9月1日、2日回校报到注册，9月3日正式上课。')
        print('    补考安排在下学期开学前一周进行，即在星期四、五、六、日四天（8月30～9月2日），有不及格科目的学生，应利用假期认真复习备考，提前回来参加补考，以取得毕业学分。')
        print('    未尽事宜请联系刘小雪老师，15123217949，QQ:85608274.')
        print(' ')




if __name__ == '__main__':
    read_excel()