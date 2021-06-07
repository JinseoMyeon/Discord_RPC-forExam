from pypresence import Presence
import time
import datetime

runtime = time.time()
clientId = "849926994971328523"

client = Presence(clientId,pipe=0)
print("[RPC] Successfully Connected")
client.connect()
whattodo6 = ["기상시간 | Woke up", "휴식 | Taking a rest", "아침학습 | Studying", "조회 | Class Starts", "1교시 | 1st Period", "쉬는시간 | Breaktime", "2교시 | 2nd Period", "쉬는시간 | Breaktime", "3교시 | 3rd Period", "쉬는시간 | Breaktime", "4교시 | 4th Period", "점심식사 | Lunchtime", "5교시 | 5th Period", "쉬는시간 | Breaktime", "6교시 | 6th Period", "종례 | Class endtime", "휴식 | Taking a rest", "휴식 | Taking a rest", "학원 | Private academy", "휴식 | Taking a rest", "저녁식사 | Dinnertime", "야간학습 | Studying", "쉬는시간 | Breaktime", "야간학습 | Studying", "취침준비 | Ready for bed"]
whattodo7 = ["기상시간 | Woke up", "휴식 | Taking a rest", "아침학습 | Studying", "조회 | Class Starts", "1교시 | 1st Period", "쉬는시간 | Breaktime", "2교시 | 2nd Period", "쉬는시간 | Breaktime", "3교시 | 3rd Period", "쉬는시간 | Breaktime", "4교시 | 4th Period", "점심식사 | Lunchtime", "5교시 | 5th Period", "쉬는시간 | Breaktime", "6교시 | 6th Period", "쉬는시간 | Breaktime", "7교시 | 7th Period", "종례 | Class endtime", "학원 | Private academy", "휴식 | Taking a rest", "저녁식사 | Dinnertime", "야간학습 | Studying", "쉬는시간 | Breaktime", "야간학습 | Studying", "취침준비 | Ready for bed"]
nowstatus = ""
nowschedule = ""
dayschedule = ""

while True:
    nowTime = time.strftime('%H%M%S')
    nowDay = datetime.datetime.today().weekday()
    ctime = datetime.datetime.now()
    cyear = ctime.year
    cmonth = ctime.month
    cday = ctime.day
    finalexam = datetime.date(2021,6,30)
    examwen = (30 - cday)
    examwen = str(examwen)
    if nowDay == 1 or 3 :
        dayschedule = whattodo7
    if nowDay == 0 or 2 or 4 :
        dayschedule = whattodo6
    elif nowDay == 5 or 6 :
        print("주말이기 때문에 스케줄을 인식할 수 없습니다.")
    
    if "065000" > nowTime > '063000' :
        nowstatus = dayschedule[0]
        timeleft = datetime.datetime(cyear,cmonth,cday,6,50)
        timeleft = timeleft.timestamp()

    if "081000" > nowTime > "065000" :
        nowstatus = dayschedule[1]
        timeleft = datetime.datetime(cyear,cmonth,cday,8,10)
        timeleft = timeleft.timestamp()

    if "085000" > nowTime > "081000" :
        nowstatus = dayschedule[2]
        timeleft = datetime.datetime(cyear,cmonth,cday,8,50)
        timeleft = timeleft.timestamp()

    if "091500" > nowTime > "085000" :
        nowstatus = dayschedule[3]
        timeleft = datetime.datetime(cyear,cmonth,cday,9,15)
        timeleft = timeleft.timestamp()

    if "100000" > nowTime > "091500" :
        nowstatus = dayschedule[4]
        timeleft = datetime.datetime(cyear,cmonth,cday,10,00)
        timeleft = timeleft.timestamp()

    if "101000" > nowTime > "100000" :
        nowstatus = dayschedule[5]
        timeleft = datetime.datetime(cyear,cmonth,cday,10,10)
        timeleft = timeleft.timestamp()

    if "105500" > nowTime > "101000" :
        nowstatus = dayschedule[6]
        timeleft = datetime.datetime(cyear,cmonth,cday,10,55)
        timeleft = timeleft.timestamp()

    if "110500" > nowTime > "105500" :
        nowstatus = dayschedule[7]
        timeleft = datetime.datetime(cyear,cmonth,cday,11,5)
        timeleft = timeleft.timestamp()

    if "115000" > nowTime > "110500" :
        nowstatus = dayschedule[8]
        timeleft = datetime.datetime(cyear,cmonth,cday,11,50)
        timeleft = timeleft.timestamp()

    if "120000" > nowTime > "115000" :
        nowstatus = dayschedule[9]
        timeleft = datetime.datetime(cyear,cmonth,cday,12,00)
        timeleft = timeleft.timestamp()

    if "124500" > nowTime > "120000" :
        nowstatus = dayschedule[10]
        timeleft = datetime.datetime(cyear,cmonth,cday,12,45)
        timeleft = timeleft.timestamp()

    if "134500" > nowTime > "124500" :
        nowstatus = dayschedule[11]
        timeleft = datetime.datetime(cyear,cmonth,cday,13,45)
        timeleft = timeleft.timestamp()

    if "143000" > nowTime > "134500" :
        nowstatus = dayschedule[12]
        timeleft = datetime.datetime(cyear,cmonth,cday,14,30)
        timeleft = timeleft.timestamp()

    if "144000" > nowTime > "143000" :
        nowstatus = dayschedule[13]
        timeleft = datetime.datetime(cyear,cmonth,cday,14,40)
        timeleft = timeleft.timestamp()

    if "152500" > nowTime > "144000" :
        nowstatus = dayschedule[14]
        timeleft = datetime.datetime(cyear,cmonth,cday,15,25)
        timeleft = timeleft.timestamp()

    if "153500" > nowTime > "152500" :
        nowstatus = dayschedule[15]
        timeleft = datetime.datetime(cyear,cmonth,cday,15,35)
        timeleft = timeleft.timestamp()

    if "162000" > nowTime > "153500" :
        nowstatus = dayschedule[16]
        timeleft = datetime.datetime(cyear,cmonth,cday,16,20)
        timeleft = timeleft.timestamp()

    if "163000" > nowTime > "162000" :
        nowstatus = dayschedule[17]
        timeleft = datetime.datetime(cyear,cmonth,cday,16,30)
        timeleft = timeleft.timestamp()

    if "180000" > nowTime > "163000" :
        nowstatus = dayschedule[18]
        timeleft = datetime.datetime(cyear,cmonth,cday,18,00)
        timeleft = timeleft.timestamp()

    if "183000" > nowTime > "180000" :
        nowstatus = dayschedule[19]
        timeleft = datetime.datetime(cyear,cmonth,cday,18,30)
        timeleft = timeleft.timestamp()

    if "195000" > nowTime > "183000" :
        nowstatus = dayschedule[20]
        timeleft = datetime.datetime(cyear,cmonth,cday,19,50)
        timeleft = timeleft.timestamp()

    if "211000" > nowTime > "195000" :
        nowstatus = dayschedule[21]
        timeleft = datetime.datetime(cyear,cmonth,cday,21,10)
        timeleft = timeleft.timestamp()

    if "213000" > nowTime > "211000" :
        nowstatus = dayschedule[22]
        timeleft = datetime.datetime(cyear,cmonth,cday,21,30)
        timeleft = timeleft.timestamp()

    if "225000" > nowTime > "213000" :
        nowstatus = dayschedule[23]
        timeleft = datetime.datetime(cyear,cmonth,cday,22,50)
        timeleft = timeleft.timestamp()

    if "235000" > nowTime > "225000" :
        nowstatus = dayschedule[24]
        timeleft = datetime.datetime(cyear,cmonth,cday,23,50)
        timeleft = timeleft.timestamp()

    if nowstatus != nowschedule :
        client.update(details="공부중인 교과 : "+ "", #details 부분만 수정해야 정상작동
                      state="시간표 : "+nowstatus,
                      large_image="books",
                      large_text="시험기간까지 D-"+examwen,
                      small_image="midigo",
                      small_text="모 학교 시간표와 맞추는 중",
                      end=timeleft)
        nowschedule = nowstatus
        print("[RPC] Schedule Changed. Now Status : "+nowstatus)
    time.sleep(1)