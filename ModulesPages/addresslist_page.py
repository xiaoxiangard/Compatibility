# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
# ͨѶ¼ҳ��
import time
from selenium.webdriver.common.by import By
from BasePages.base_page import BasePage
from ModulesPages.addmember_page import AddMemberPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddressListPage(BasePage):

    def goto_addmember(self):
        # ������ӳ�Աҳ��,��ӳ�Ա��ť����δ����ȫ����Ҫ�ȴ�
        time.sleep(10)
        self.find_and_click(By.XPATH,
                            "//div[@class='ww_operationBar']//a[contains(@class,'js_add_member')]")
        return AddMemberPage(self.driver)

    def get_list(self):
        # ҳ��Ԫ��δ����ȫ��ʹ����ʾ�ȴ�����Ԫ��
        loc = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        # ����Ԫ��, ����List[WebElement]
        name_ele = self.driver.find_elements(*loc)
        # List[WebElement] -> WebElement
        name_list = [web_ele.text for web_ele in name_ele]
        return name_list
