# ttt.py
"""
1.3 숫자

***연습 문제 1.7: 데이브의 주택 담보 대출***
데이브는 500,000 달러의 30년 고정 이율 주택 담보 대출(mortgage)을 받기로 결정했다.
이율은 5%이고 매달 납부할 금액은 2684.11 달러다.
다음은 대출 기간 동안 지불할 총액을 계산하는 프로그램이다.
남은 원금 = 전달 원금 * (1+년이자/12) - 월납입금
총납입금 = 전달 총납입금 + 이번달 월납입금

***study***
round(number, option) 반올림, 올림, 내림
format(number, ',') 숫자 천단위마다 , 삽입
관련정보 : https://cosmosproject.tistory.com/373
"""

principal   = 500000.0
rate        = 0.05
payment     = 2684.11
total_paid  = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', format(round(total_paid, 1), ','))
# **study**
print('이 파일의 경로는 아래와 같습니다.\n', __file__)  # 이 파일의 절대 경로 반환
