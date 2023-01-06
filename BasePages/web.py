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

    # 启动浏览器
    def start(self, browser, web_url=None):

        if self.driver is None:
            # 第一次实例化,第一次扫码登陆，获取cookie，记录文件中
            logging.info(f"实例化 driver .")
            if web_url is not None:
                driver, cookie_path = self.get_path(browser)
                self.driver = driver
                self.driver.implicitly_wait(5)
                self.driver.maximize_window()
                # 当cookie_path文件不存在 或者 cookie文件超过有效期，请先删除cookie_path文件,再执行get_cookies操作
                self.get_cookies(web_url, cookie_path)
                # 非第一次扫码登陆或者cookie还在有效期内，无需扫码登陆，植入cookie登陆
                # self.add_cookie(web_url, cookie_path)
            else:
                # 如果url 为空，那么抛出异常
                logging.info(f"url 为空，直接退出")
                self.stop()
        else:
            logging.info(f"复用 driver .")
            # driver已实例，无需扫码，直接获取web_url
            if web_url is not None:
                self.driver.get(web_url)
                self.driver.implicitly_wait(5)
            else:
                # 如果url 为空，那么抛出异常
                logging.info(f"url 为空，直接退出")
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
        # 访问主页
        self.driver.get(web_url)
        # 等待20S 扫码登陆
        time.sleep(20)
        # 登陆成功之后，再去获取cookie信息
        cookie = self.driver.get_cookies()
        # 获取cookie文件路径
        logging.info(f"获取cookie文件路径: {cookie_path}")
        # 将cookie写入文件中
        with open(cookie_path, "w") as f:
            yaml.safe_dump(cookie, f)
        logging.info(f"cookie写入文件成功")

    def add_cookie(self, web_url=None, cookie_path=None):
        # 访问主页
        self.driver.get(web_url)
        # 定义cookie，先手动粘贴
        cookie = yaml.safe_load(open(cookie_path, "r"))
        # 植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(5)
        logging.info(f"植入cookie成功")
        # 再次访问页面,无需扫码
        self.driver.get(web_url)
