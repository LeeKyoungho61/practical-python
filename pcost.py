# pcost.py

"""
매수가격 계산



***연습 문제 1.30: 스크립트를 함수로 탈바꿈***
연습 문제 1.27의 pcost.py 프로그램 코드를 가져다가 portfolio_cost(filename) 함수를 만들어 보라.
이 함수는 파일명을 입력으로 받아 포트폴리오 데이터를 읽고, 포트폴리오의 총 비용을 부동소수점으로 반환한다.

***연습 문제 1.28: 다른 종류의 "파일"***
일반 텍스트 파일이 아닌, gzip 압축된 데이터 파일을 읽고 싶으면 어떻게 해야 할까?
빌트인 open() 함수는 여기서 도움이 되지 않지만,
파이썬에는 gzip 압축된 파일을 읽을 수 있는 gzip 라이브러리 모듈이 있다.

***연습 문제 1.27: 데이터 파일 읽기***
portfolio.csv의 각 컬럼은 보유 종목의 이름, 주식 수, 매수가격에 해당한다.
이 파일을 열어 전체 행을 읽은 뒤,
포트폴리오의 전체 주식을 매수하는데 드는 비용을 계산하는 pcost.py 프로그램을 작성한다.
"""

import csv
# csv 모듈은 따옴표라든지, 콤마를 사용한 분할 등 저수준의 여러 가지 세부사항을 처리해준다


def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt', encoding='UTF-8') as f:
        rows    = csv.reader(f)             # csv모듈로 콤마 자동처리 시킨다
        headers = next(f)

        for row in rows:                    # row = ['"AA"', '100', '32.20'] 리스트로 변환
            try:
                nshare      = int(row[1])       # 두번째 컬럼 = 수량
                price       = float(row[2])     # 세번째 컬럼 = 매수단가
                cost        = nshare * price    # 매수가격 = 수량 * 매수단가
                total_cost  += cost
            except ValueError:
                print("Bad row:", row)

    return total_cost


import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')


cost = portfolio_cost(filename)
print("Total cost:", cost)
