# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
from selenium.webdriver.common.by import By
from BasePages.base_page import BasePage
from ModulesPages.addmember_page import AddMemberPage
from ModulesPages.addresslist_page import AddressListPage


class MainPage(BasePage):

    def goto_addmember(self):
        # 进入添加成员页面
        self.find_and_click(By.CSS_SELECTOR, ".ww_indexImg_AddMember")
        return AddMemberPage(self.driver)

    def goto_addresslist(self):
        # 进入通讯录页面
        self.find_and_click(By.XPATH, "//a[@id='menu_contacts']")
        return AddressListPage(self.driver)
