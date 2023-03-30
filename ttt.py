# ttt.py
"""
1.3 숫자

***연습 문제 1.8: 추가 납입***
데이브가 처음 12개월 동안 매달 1000 달러를 추가로 납입한다면 어떻게 될까?
이 추가 납입금 계산을 포함하도록 프로그램을 수정해 총 납입금액과 소요 월수를 프린트해보자.
프로그램을 실행했을 때 총 납입금이 929,965.62, 소요 월수는 342로 나와야 한다.

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
# 연습문제 1.7
principal   = 500000.0
rate        = 0.05
payment     = 2684.11
total_paid  = 0.0

# 연습문제 1.8
extra_payment = 1000    # 추가 월납입금
exp_month     = 12      # 추가 납입금 개월
payment_month = 0       # 총 납입 개월

# 12개월 동안 실행
while exp_month > 0:
    principal = principal * (1+rate/12) - (payment + extra_payment)
    exp_month -= 1
    payment_month += 1
    total_paid = total_paid + (payment + extra_payment)

# 원금 다 갚을때까지 실행
while principal > 0:
    principal = principal * (1+rate/12) - payment
    payment_month += 1
    total_paid = total_paid + payment

print('Total paid', format(round(total_paid, 1), ','))
print('Total month', payment_month)
# **study**
print('이 파일의 경로는 아래와 같습니다.\n', __file__)  # 이 파일의 절대 경로 반환
