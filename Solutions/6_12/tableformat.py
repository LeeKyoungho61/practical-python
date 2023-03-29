# tableformat_410.py
"""
405 : 클래스 적용(220815)
410 : 사용자 정의 어트리뷰트를 보여주는 테이블을 만든다. getattr 적용(220816)
"""


class TableFormatter:
    def headings(self, headers):
        """
        테이블 헤딩을 반환
        :param headers:
        :return:
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        테이블 데이터의 단일 행을 반환
        :param rowdata:
        :return:
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    """
    테이블을 일반 텍스트 포맷으로 출력
    """
    def headings(self, headers):
        """
        받은 헤더를 텍스트 포맷으로 인쇄
        :param headers: 헤더(컬럼) 이름들
        :return: 없다. 프린트한다
        """
        for h in headers:  # 각 컬럼 모두에 대해서 프린트
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(name):
    '''
    Create an appropriate formatter given an output format name
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [ str(getattr(obj, name)) for name in columns ]
        formatter.row(rowdata)

