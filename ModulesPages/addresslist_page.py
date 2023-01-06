# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
# 通讯录页面
import time
from selenium.webdriver.common.by import By
from BasePages.base_page import BasePage
from ModulesPages.addmember_page import AddMemberPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddressListPage(BasePage):

    def goto_addmember(self):
        # 进入添加成员页面,添加成员按钮属性未加载全，需要等待
        time.sleep(10)
        self.find_and_click(By.XPATH,
                            "//div[@class='ww_operationBar']//a[contains(@class,'js_add_member')]")
        return AddMemberPage(self.driver)

    def get_list(self):
        # 页面元素未加载全，使用显示等待查找元素
        loc = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        # 查找元素, 返回List[WebElement]
        name_ele = self.driver.find_elements(*loc)
        # List[WebElement] -> WebElement
        name_list = [web_ele.text for web_ele in name_ele]
        return name_list
