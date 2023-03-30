# ttt.py
"""
1.4 문자열

"""

"""
***문자열 이스케이프 코드(escape code)***
'\n'      라인 피드(Line feed)
'\r'      캐리지 리턴(Carriage return)
'\t'      탭(Tab)
'\''      작은따옴표(Literal single quote)
'\"'      큰따옴표(Literal double quote)
'\\'      백슬래시(Literal backslash)
"""

"""
***문자열 메서드***
s.endswith(suffix)     # 문자열이 suffix로 끝나는지 확인
s.find(t)              # s에서 t가 처음 나타나는 곳
s.index(t)             # s에서 t가 처음 나타나는 곳
s.isalpha()            # 문자가 영문자인지 여부
s.isdigit()            # 문자가 숫자인지 여부
s.islower()            # 문자가 소문자인지 여부
s.isupper()            # 문자가 대문자인지 여부
s.join(slist)          # s를 구분자(delimiter)로 삼아 문자열의 리스트를 붙이기(join)
s.lower()              # 소문자로 변환
s.replace(old,new)     # 텍스트 교체
s.rfind(t)             # 문자열의 끝에서부터 t를 검색
s.rindex(t)            # 문자열의 끝에서부터 t를 검색
s.split([구분자])       # 문자열을 분할해 부분 문자열의 리스트를 만듦
s.startswith(prefix)   # 문자열이 prefix로 시작하는지 확인
s.strip()              # 앞뒤의 공백을 제거
s.upper()              # 대문자로 변환
"""

"""
***원시 문자열(Raw String)***
원시 문자열은 백슬래시를 해석하지 않는 문자열 리터럴이다. 소문자 "r"을 앞에 붙여 원시 문자열임을 나타낸다.
rs = r'c:\newdata\test' # 원시(백슬래시를 해석하지 않음)
"""

"""
***f 문자열(f-String)***
a = f'{name:>10s} {shares:10d} {price:10.2f}'
"""