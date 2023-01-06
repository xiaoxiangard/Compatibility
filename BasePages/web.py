# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import logging
import time
import yaml
from selenium import webdriver
from BasePages.base_page import BasePage
from ModulesPages.main_page import MainPage


class Web(BasePage):
    _cookie_path = None

    # ���������
    def start(self, browser, web_url=None):

        if self.driver is None:
            # ��һ��ʵ����,��һ��ɨ���½����ȡcookie����¼�ļ���
            logging.info(f"ʵ���� driver .")
            if web_url is not None:
                driver, cookie_path = self.get_path(browser)
                self.driver = driver
                self.driver.implicitly_wait(5)
                self.driver.maximize_window()
                # ��cookie_path�ļ������� ���� cookie�ļ�������Ч�ڣ�����ɾ��cookie_path�ļ�,��ִ��get_cookies����
                self.get_cookies(web_url, cookie_path)
                # �ǵ�һ��ɨ���½����cookie������Ч���ڣ�����ɨ���½��ֲ��cookie��½
                # self.add_cookie(web_url, cookie_path)
            else:
                # ���url Ϊ�գ���ô�׳��쳣
                logging.info(f"url Ϊ�գ�ֱ���˳�")
                self.stop()
        else:
            logging.info(f"���� driver .")
            # driver��ʵ��������ɨ�룬ֱ�ӻ�ȡweb_url
            if web_url is not None:
                self.driver.get(web_url)
                self.driver.implicitly_wait(5)
            else:
                # ���url Ϊ�գ���ô�׳��쳣
                logging.info(f"url Ϊ�գ�ֱ���˳�")
                self.stop()

        return self

    def stop(self):
        self.driver.quit()

    def go_main(self):
        return MainPage(self.driver)

    def get_path(self, browser=None):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
            self._cookie_path = "../data/cookie_firefox.yaml"
        elif browser == "edge":
            self.driver = webdriver.Edge()
            self._cookie_path = "../data/cookie_edge.yaml"
        else:
            self.driver = webdriver.Chrome()
            self._cookie_path = "../data/cookie_chrome.yaml"
        return self.driver, self._cookie_path

    def get_cookies(self, web_url=None, cookie_path=None):
        # ������ҳ
        self.driver.get(web_url)
        # �ȴ�20S ɨ���½
        time.sleep(20)
        # ��½�ɹ�֮����ȥ��ȡcookie��Ϣ
        cookie = self.driver.get_cookies()
        # ��ȡcookie�ļ�·��
        logging.info(f"��ȡcookie�ļ�·��: {cookie_path}")
        # ��cookieд���ļ���
        with open(cookie_path, "w") as f:
            yaml.safe_dump(cookie, f)
        logging.info(f"cookieд���ļ��ɹ�")

    def add_cookie(self, web_url=None, cookie_path=None):
        # ������ҳ
        self.driver.get(web_url)
        # ����cookie�����ֶ�ճ��
        cookie = yaml.safe_load(open(cookie_path, "r"))
        # ֲ��cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(5)
        logging.info(f"ֲ��cookie�ɹ�")
        # �ٴη���ҳ��,����ɨ��
        self.driver.get(web_url)
