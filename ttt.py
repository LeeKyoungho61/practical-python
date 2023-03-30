# ttt.py
"""
1.5 리스트
기호: []
어떤 타입이든 리스트 항목(item)이 될 수 있다.
리스트의 항목을 변경할 수 있다.
리스트에는 중복된 값이 들어가도 전혀 문제가 없다.

"""

"""
1.6 파일 관리
파일을 연다.
f = open('foo.txt', 'rt')     # 읽기를 위해 열기(텍스트)
g = open('bar.txt', 'wt')     # 쓰기를 위해 열기(텍스트)

모든 데이터를 읽는다.
data = f.read()

텍스트를 기록한다.
g.write('some text')

마쳤으면 파일을 닫는다.
f.close()
"""

"""
***파일 데이터를 읽는 일반적인 방법***
파일 전체를 한번에 읽어 문자열로 처리한다.
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data`는 `foo.txt`의 텍스트 전체로 된 문자열이다
    
파일을 한 행씩 읽어 내려가기.
with open(filename, 'rt') as file:
    for line in file:
        # 행을 처리


***파일에 쓰는 일반적인 방법***
1. 문자열 데이터를 기록한다.
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
    ...
    
2. print 함수의 출력을 재지정(redirect)한다.
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
    ...
"""