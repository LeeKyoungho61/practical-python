# ttt.py
"""
12. 첫번째 프로그램 - python 특징 알아보기

어느 날 아침, 당신은 시카고의 시어스 타워(Sears tower) 근처를 거닐다가 보도에 1 달러 지폐를 한 장 올려뒀다.
그 후 매일 외출할 때마다 그 위에 지폐를 얹어 탑을 쌓으며, 높이는 매일 두 배로 불어난다.
돈으로 쌓은 탑의 높이가 시어스 타워의 높이와 같아지려면 시간이 얼마나 걸릴까?
"""

bill_thickness = 0.11 * 0.001  # 지페의 두께(0.11 mm)를 미터로 환산
sears_hight    = 442           # 높이(미터)
num_bills      = 1             # 지폐숫자 초기값
day            = 1             # 일 초기값

while num_bills * bill_thickness < sears_hight:  # sears 빌딩보다 낮을동안 아래 실행
    print(day, num_bills, num_bills * bill_thickness)  # 결과 (먼저) 출력
    day += 1  # 일수 증가
    num_bills = num_bills * 2  # 지폐갯수 날마다 2배 증가

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
