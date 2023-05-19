# pcost.py

"""
매수가격 계산

"""

"""
***연습 문제 1.28: 다른 종류의 "파일"***
일반 텍스트 파일이 아닌, gzip 압축된 데이터 파일을 읽고 싶으면 어떻게 해야 할까? 
빌트인 open() 함수는 여기서 도움이 되지 않지만, 파이썬에는 gzip 압축된 파일을 읽을 수 있는 gzip 라이브러리 모듈이 있다.
***연습 문제 1.27: 데이터 파일 읽기***
portfolio.csv의 각 컬럼은 보유 종목의 이름, 주식 수, 매수가격에 해당한다.
이 파일을 열어 전체 행을 읽은 뒤, 포트폴리오의 전체 주식을 매수하는데 드는 비용을 계산하는 pcost.py 프로그램을 작성한다.
"""

with open('data/portfolio.csv', 'rt') as f:
    headers = next(f)
    total_cost = 0

    for line in f:                          # line = '"AA",100,32.20'(문자)
        row = line.split(',')               # row = ['"AA"', '100', '32.20'] 리스트로 변환(각 항목은 여전히 문자)
        # cost = int(row[1]) * float(row[2])  # 정수, 실수로 데이터를 변환해야 계산 가능해 진다
        nshare = int(row[1])                # 두번째 컬럼 = 수량
        price  = float(row[2])              # 세번째 컬럼 = 매수단가
        cost   = nshare * price             # 매수가격 = 수량 * 매수단가
        total_cost = total_cost + cost

    print(f'Total cost {total_cost}')
