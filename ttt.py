"""
작성일자:
내용  : 이 함수는 지난 연습 문제의 첫 번째 제너레이터 예제와 거의 같지만,
        파일을 열지 않고 인자로 받은 행들의 시퀀스에 대해서만 연산을 한다.
"""


def countdown(n):
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1


# 파일을 받아서 파일에 특정문자가 있으면 해당 행을 반환
# 파일 대신 인자로 받는다
def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


# for x in countdown(10):
#     print(x, end=" ")
