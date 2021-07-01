# -*- coding:utf-8 -*-
import pytest
import xlrd


def get_excel_data():
    file = 'test.xls'
    filename = xlrd.open_workbook(file)
    sheet = filename.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    lst = []
    # for row in range(rows):
    #     for col in range(cols):
    #         cell_data = sheet.cell_value(row, col)
    #         lst.append(cell_data)
    # return lst
    for row in range(rows):
        row_data = sheet.row_values(row)
        row_data = tuple(row_data)
        lst.append(row_data)
    return lst


@pytest.mark.parametrize('username, email, pwd, confirmPwd, captcha, expected', get_excel_data())
def test01(username, email, pwd, confirmPwd, captcha, expected):
    print(username, email, pwd, confirmPwd, captcha, expected)


if __name__ == '__main__':
    pytest.main('-sv', 'test_excel.py')
