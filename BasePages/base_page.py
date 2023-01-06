# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
# ��װ����ҳ������ԵĲ���������driver ��ʵ����
import logging
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator=None):
        logging.info(f"��λ��:{by}, ��λ���ʽ: {locator}")
        # ����Ԫ��,����WebElement
        # �������һ��������֤����Ԫ��
        if locator is None:
            # �������Ԫ�棬�����������
            res = self.driver.find_element(*by)
        # �����������������֤���Ƿֿ����ݵ�
        else:
            res = self.driver.find_element(by, locator)
        return res

    def find_and_click(self, by, locator=None):
        logging.info(f"�������:")
        # �ҵ�Ԫ�ز����
        self.find(by, locator).click()

    def find_and_send(self, by, locator=None, text=None):
        logging.info(f"�������,��������Ϊ: {text}")
        # �ҵ�Ԫ�ز�����
        self.find(by, locator).send_keys(text)

    def find_and_clear(self, by, locator=None):
        logging.info(f"clear����")
        # �ҵ�Ԫ�ز�����
        self.find(by, locator).clear()
