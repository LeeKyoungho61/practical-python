# pcost.py

"""
매수가격 계산

"""

"""
연습 문제 1.27: 데이터 파일 읽기
portfolio.csv의 각 컬럼은 보유 종목의 이름, 주식 수, 매수가격에 해당한다.
이 파일을 열어 전체 행을 읽은 뒤, 포트폴리오의 전체 주식을 매수하는 데 드는 비용을 계산하는 pcost.py 프로그램을 작성한다.
"""

with open('data/portfolio.csv', 'rt') as f:
    headers = next(f)

    for line in f:                          # line = '"AA",100,32.20'(문자)
        row = line.split(',')               # row = ['"AA"', '100', '32.20'] 리스트로 변환(각 항목은 여전히 문자)
        # cost = int(row[1]) * float(row[2])  # 정수, 실수로 데이터를 변환해야 계산 가능해 진다
        nshare = int(row[1])
        price  = float(row[2])
        cost   = nshare * price

    print(cost)
