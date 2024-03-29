# -*- coding:utf-8 -*-
from testcases.basic.test_user_register import TestUserRegister
from testcases.basic.test_user_login import TestUserLogin
from testcases.basic.test_admin_login import TestAdminLogin
from testcases.basic.test_category import TestCategory
from testcases.basic.test_article import TestArticle
if __name__ == '__main__':
    # driver = webdriver.Firefox()
    # driver.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')
    # print(get_code(driver, 'imgCode'))
    # case = TestUserRegister()
    # case.test_register_code_error()
    # case.test_register_ok()
    # case = TestUserLogin()
    # case.test_user_login_username_error()
    # case.test_user_login_ok()
    case = TestAdminLogin()
    # case.test_admin_login_username_error()
    case.test_admin_login_ok()
    # result = TestCategory(case)
    # result.test_add_category_error()
    # result.test_add_category_ok()
    result = TestArticle(case)
    result.test_add_ok()
    # result.test_delete_one_article_ok()
    # result.test_delete_all_article_ok()
