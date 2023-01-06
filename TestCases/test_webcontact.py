# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import logging
import os
from BasePages.web import Web
from Utils.generate_info import GenerateInfo


class TestContact:
    _browser = None
    _web_url = r'https://work.weixin.qq.com/wework_admin/frame#index'

    def setup_class(self):
        # ʵ����web
        self.web = Web()
        self._browser = os.getenv("env").strip('"')

    def setup(self):
        browser = self._browser
        web_url = self._web_url
        self.main = self.web.start(browser, web_url).go_main()

    def teardown_class(self):
        self.web.stop()

    def test_addcontact(self):
        name = GenerateInfo.get_name()
        phone_num = GenerateInfo.get_phonenum()
        acc_id = GenerateInfo.get_accid()
        logging.info(f"�����ϵ������: {name}, �����ϵ���˺�: {acc_id}, �����ϵ���ֻ�����: {phone_num} ")
        # ������ҳ��->�����ӳ�Ա->������ӳ�Աҳ��->�����Ա��Ϣ->�������->����ͨѶ¼ҳ��->��ȡ���
        result = self.main.goto_addmember().add_member(name, acc_id, phone_num).get_list()
        assert name in result

    def test_addcontact2(self):
        name = GenerateInfo.get_name()
        phone_num = GenerateInfo.get_phonenum()
        acc_id = GenerateInfo.get_accid()
        logging.info(f"�����ϵ������: {name}, �����ϵ���˺�: {acc_id}, �����ϵ���ֻ�����: {phone_num} ")
        # ������ҳ��->����ͨѶ¼ҳ��->�����ӳ�Ա->������ӳ�Աҳ��->�����Ա��Ϣ->�������->����ͨѶ¼ҳ��->��ȡ���
        result = self.main.goto_addresslist().goto_addmember().\
            add_member(name, acc_id, phone_num).get_list()
        assert name in result
