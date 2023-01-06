# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
# ��ӳ�Աҳ��
from selenium.webdriver.common.by import By
from BasePages.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member(self, name, acc_id, phone_num):
        # input name
        self.find_and_send(By.ID, "username", name)
        # input acc_id ����������Ԫ��Ҫ�ȵ�����ܱ���ֵ
        self.find_and_click(By.ID, "memberAdd_acctid")
        self.find_and_clear(By.ID, "memberAdd_acctid")
        self.find_and_send(By.ID, "memberAdd_acctid", acc_id)
        # input phone_num
        self.find_and_send(By.ID, "memberAdd_phone", phone_num)
        # click save
        self.find_and_click(By.CSS_SELECTOR, ".js_btn_save")

        # ѭ�����룺ȫ�ֵ���ᱨ���ĳɾֲ�����
        from ModulesPages.addresslist_page import AddressListPage
        return AddressListPage(self.driver)
