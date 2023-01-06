# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
# 封装所有页面对象共性的操作，比如driver 的实例化
import logging
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator=None):
        logging.info(f"定位符:{by}, 定位表达式: {locator}")
        # 查找元素,返回WebElement
        # 如果传入一个参数，证明是元祖
        if locator is None:
            # 如果传入元祖，则做解包操作
            res = self.driver.find_element(*by)
        # 如果传入两个参数，证明是分开传递的
        else:
            res = self.driver.find_element(by, locator)
        return res

    def find_and_click(self, by, locator=None):
        logging.info(f"点击操作:")
        # 找到元素并点击
        self.find(by, locator).click()

    def find_and_send(self, by, locator=None, text=None):
        logging.info(f"输入操作,输入内容为: {text}")
        # 找到元素并输入
        self.find(by, locator).send_keys(text)

    def find_and_clear(self, by, locator=None):
        logging.info(f"clear操作")
        # 找到元素并输入
        self.find(by, locator).clear()
