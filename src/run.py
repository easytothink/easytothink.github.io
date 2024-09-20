from datetime import datetime
import pylightxl as xl

def calc_delta_time(time_str1,time_str2): 
    if (time_str1=='' or time_str2==''):
        return 0
    hour1, minute1 = map(int, time_str1.split(':'))
    hour2, minute2 = map(int, time_str2.split(':'))
    
    time1=hour1*60+minute1
    time2=hour2*60+minute2

    if (time1<time2):
        if(time1<420):
            time1=420
        if(time2>510):
            time2=510
        return time2-time1
    return 0
  

def title(owb):
    title = ["姓名","出勤天数","缺勤天数","打卡时长","换算时长","集体晚自习","总时长"]
    for col_id, data in enumerate(title, start=1):                                                      owb.ws(owb.ws_names[0]).update_index(row=1, col=col_id, val=data)

    return owb

if __name__ == '__main__':
    vacation=[]
    print("请输入假期日期（输入#来停止）：")
    temp = input()
    while(temp!="#"):
        vacation.append(temp)
        temp=input()

    print("请输入集体晚自习时长（单位：时）：")
    night_hour=float(input())
    #print(vacation)

    iwb = xl.readxl(fn="book.xlsx")
    iws = iwb.ws(iwb.ws_names[0])

    name_list = list(set(iws.col(1)))
    name_list.pop(0)
    #print(name_list)

    owb = xl.Database()                                                                             
    owb.add_ws("统计情况")                                                                          
    owb = title(owb)                        

    for name in name_list:
        score = 0
        success_count=0
        fail_count=0
        for row in iws.rows:
            if(row[0] == name):
                #计算打卡时长
                score+=calc_delta_time(row[9], row[11])
                #计算出勤
                if(row[9]!=''):
                    success_count+=1

                #计算缺勤
                data = row[6]
                flag = True
                if('六' in data or '日' in data):
                    flag = False
                for day in vacation:
                    if(day in data):
                        flag = False
                #print(flag)
                if(flag and row[9] == ''):
                    fail_count+=1
             
        row_list=[name,success_count,fail_count,score,round(score/60,2),night_hour,round(score/60+night_hour,2)]
        print(row_list)

        for col_id, row_data in enumerate(row_list, start=1):                                               owb.ws(owb.ws_names[0]).update_index(row=name_list.index(name)+2, col=col_id, val=row_data)

    xl.writexl(db=owb, fn="output.xlsx")
