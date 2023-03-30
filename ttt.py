# ttt.py
"""
1.3 숫자

***연습 문제 1.10: 테이블 만들기***
월수, 현재까지의 납부액, 남은 원금을 나타내는 테이블을 프린트하게 프로그램을 수정해 보라.
마지막 달에 초과 납부하는 금액이 생기지 않게 프로그램을 수정해 보라.

***연습 문제 1.9: 추가 납입금 계산기***
추가 납입금을 일반적으로 다룰 수 있게 프로그램을 수정하자.
사용자가 다음 변수를 설정할 수 있게 한다.
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

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
https://cosmosproject.tistory.com/373
https://m.blog.naver.com/hankrah/221457221963
"""
# 연습 문제 1.7: 데이브의 주택 담보 대출
principal   = 500000.0
rate        = 0.05
payment     = 2684.11
total_paid  = 0.0

# 연습문제 1.8: 추가 납입
# extra_payment = 1000    # 추가 월납입금
# exp_month     = 12      # 추가 납입금 개월
payment_month = 0       # 총 납입 개월

# 연습문제 1.9: 추가 납입금 계산기
extra_payment_start_month = 61  # 추가 납입 시작 월
extra_payment_end_month = 108   # 추가 납입 종료 월
extra_payment = 1000            # 추가 납입 금액

# 연습문제 1.10: 테이블 만들기
# 연습문제 1.11: 마지막달 에러 바로잡기

# 원금 다 갚을때까지 실행
while principal > 0:
    payment_month += 1
    if principal > payment:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    else:
        principal = principal * (1 + rate / 12)
        total_paid = total_paid + principal
        payment = principal
        principal -= principal

    # 추가 납입으로 설정한 월만 실행
    if extra_payment_start_month <= payment_month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(f'{payment_month:>3,} {payment:>15,.2f} {total_paid:>15,.2f} {principal:>15,.2f}')

print('Total paid', format(round(total_paid, 2), ','))
print('Total month', payment_month)
# **study**
print('이 파일의 경로는 아래와 같습니다.\n', __file__)  # 이 파일의 절대 경로 반환
