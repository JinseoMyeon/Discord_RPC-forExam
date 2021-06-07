안녕하세요 진서면입니다!
무려 기말고사가 1달도 채 남지 않은 새끼가 이지랄하고 있긴 한 게 어이가 없긴 한데 대충 만들어봤습니다
디스코드 Rich Presence 기능을 이용하여 시간표를 자동으로 체크하고 바꾸게 해보았습니다.
물론 details의 "공부하는 교과 :" 부분은 수동으로 수정해줘야 합니다만.... 시험 끝나면 한번 GUI라도 만들어볼 생각이 있으니...


근데 설마 지금 쓰신다는 분은 없으시겠죠???
이런 허접하고 꼬여있는 코드로 이루어진 이런 프로그램을 쓰실 분이 계실 진 모르겠다만 간단히 사용설명을 드리자면

whattodo6, whattodo7은 6교시/7교시 대비 시간표입니다. 본인 스케줄에 맞게 적어주시면 되고요. 중요한 건 여기 적은 내용이 그대로 state의 "시간표" 부분에 들어가니 참고해주세요.
참고로 8교시나 5교시, 혹은 이외 여러가지가 존재한다면
whattodo8 = ["내용1","내용2","내용3","내용4..."] 또는 whattodo5 = ["내용1","내용2","내용3","내용4..."]
방식으로 추가해주시면 됩니다.

while True: 부분 밑에 존재하는 변수들은 일단 넘기시고, nowDay 변수는 본인이 어느 요일에 어떤 시간표를 사용하는 지에 맞춰 집어넣어주시면 됩니다.
예를 들어 월요일, 수요일, 금요일에는 7교시, 화요일, 목요일에는 5교시를 한다면
    if nowDay == 1 or 3 :
        dayschedule = whattodo5
    if nowDay == 0 or 2 or 4 :
        dayschedule = whattodo7
방식으로 넣어주시면 됩니다. (물론 이딴 식으로 스케줄 계획하는 학교는 없을거라 예상합니다.)
nowDay가 5거나 6인 경우는 토요일, 일요일을 의미하니 주말에 따로 정해진 스케줄이 없다면 무시하셔도 됩니다.

여담으로 0부터 시작해서 월요일, 화요일, 수, 목, 금, 토, 일요일 6까지로 이루어져 있습니다.
화요일 = 1, 토요일 = 5 이런 식이죠

이후 나오는 수많은 건...
if "스케줄종료시간" > nowTime > "스케줄시작시간" :
    nowstatus = dayschedule[스케줄번호,0부터시작]
    timeleft = datetime.datetime(cyear,cmonth,cday,스케줄종료종료시간,스케줄종료분)
    timeleft = timeleft.timestamp()
식으로 두시면 됩니다. 스케줄번호는 위에 whattodo 변수에 써놨던 순서로 잡히니 참고해주세요.
"반드시 whattodo 변수에 적어둔 내용의 개수보다 < nowstatus = dayschedule[스케줄번호] >에 있는 스케줄번호가 더 크면 안됩니다." 값을 찾을 수 없다며 오류나요.

한차례 노가다를 끝내셨다면 마지막 부분입니다.
        if nowstatus != nowschedule :
            client.update(details="공부중인 교과 : "+ "",
                      state="시간표 : "+nowstatus,
                      large_image="books",
                      large_text="시험기간까지 D-"+examwen,
                      small_image="midigo",
                      small_text="모 학교 시간표와 맞추는 중",
                      end=timeleft)
            nowschedule = nowstatus
            print("[RPC] Schedule Changed. Now Status : "+nowstatus
부분은 비교적 간단합니다. details는 공부중인 교과 뒤에 있는 "" 부분만 수정해주세요. 본인이 무슨 공부를 하고 있는 지 띄울 수 있습니다.
small_image, small_text는 원하는 대로 설정하실 수 있지만, 저는 "books" 와 "midigo" 두 개만 에셋에 넣어뒀으니 알아서 취향껏 해주시면 되겠습니다 :P
end=timeleft는 남은 시간이 얼마나 되는지 표시하는 것이니 가볍게 무시해주세요.

사실 제 코딩실력과 설명실력이 이정도밖에 안되서 그렇지 마개조를 하실 수 있는 분이라면 자유롭게 뜯고 씹고 맛보고 즐겨도 됩니다.
그럼 이만 공부하러 가야죠.....

* Readme for foreigners? USE GOOGLE TRANSLATE
