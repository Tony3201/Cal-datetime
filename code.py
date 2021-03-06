方法一：简单日期天数时间差计算
#!/usr/bin/env python3
from datetime import datetime
a = datetime(2021, 2, 29)
b = datetime(2025, 11, 29)
print(a)
print(b)
print("运行时间："+str((b-a).days)+" 天")

方法二：

具体如下：
#!/usr/bin/env python3
import time as t
import datetime as d
#定义时间差函数
def myDate(date1, date2):
    date1 = t.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = t.strptime(date2, "%Y-%m-%d %H:%M:%S")

    startTime = t.strftime("%Y-%m-%d %H:%M:%S", date1)
    endTime = t.strftime("%Y-%m-%d %H:%M:%S", date2)

    startTime = d.datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S")
    endTime = d.datetime.strptime(endTime,"%Y-%m-%d %H:%M:%S")
    date = endTime- startTime
    return date

#参数赋值
date1 = "2020-01-29 16:31:31"
date2 = "2025-01-23 15:30:30"
#获得时间差秒数
seconds = myDate(date1, date2).seconds
#获得时间差
date = myDate(date1, date2)
print(seconds)
print(date)

