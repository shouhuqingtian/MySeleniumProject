# -*- coding:utf-8 -*-
import pytest
import xlrd


def get_data():
    file = 'test.xls'
    filename = xlrd.open_workbook(file)
    sheet = filename.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    lst = []
    for row in range(rows):
        for col in range(cols):
            print(row, col)
            cell_data = sheet.cell_value(row, col)
            lst.append(cell_data)
    return lst


@pytest.mark.parametrize('name', get_data())
def test01(name):
    print(name)


if __name__ == '__main__':
    pytest.main('-sv', 'test_excel.py')
