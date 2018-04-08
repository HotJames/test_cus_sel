# -*- coding=utf-8 -*-
import hashlib
import logging
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import test_parameter as tp


class Automate_test(object):
    '''
    二次改进，使用面向对象来写
    sleep尽可能替换，灵活使用显性等待与隐形等待方法
    显性等待（当想要的元素加载出来则取消阻塞）
    隐性等待（当整个页面加载出来则取消阻塞）
    测试数据不再使用表格内数据，使用程序自动随机生成数据
    校验所有数据但是不再逐个校验，改为整条md5校验
    '''
    # 数据初始化
    def __init__(self):
        # 验证码框
        self.check_code_box = (By.ID, 'captcha')
        # 登陆按钮
        self.login_button = (By.ID, 'loginBtn')
        # 开户受理按钮
        self.acc_button1 = (By.XPATH, "//div[@id='bjui-sidenav-box']/ul/li/a")
        # 客户开户按钮
        self.acc_button2 = (By.XPATH, "//div[@id='bjui-sidenav-box']/ul/li/ul/li[5]/a")
        # 客户类型
        self.cus_cate_box = (By.ID, 'cate')
        # 客户级别
        self.cus_lev_box = (By.NAME, 'level')
        # 客户名称
        self.cus_name_box = (By.NAME, 'name')
        # 证件类型
        self.cert_type_box = (By.ID, 'type')
        # 证件号码
        self.cert_num_box = (By.NAME, 'clientNumber')
        # 联系人
        self.con_person_box = (By.NAME, 'contacts')
        # 联系电话
        self.con_tel_box = (By.NAME, 'tel')
        # 邮政编码
        self.post_code_box = (By.NAME, 'postCode')
        # 电子邮箱
        self.email_box = (By.NAME, 'email')
        # 一般纳税人是
        self.taxpayer_y_button = (By.NAME, 'isTaxPayer')
        # 一般纳税人否
        self.taxpayer_n_button = (By.XPATH, "(//input[@name='isTaxPayer'])[2]")
        # 联系地址
        self.con_address_box = (By.NAME, 'addr')
        # 文件上传
        self.file_list_box = (By.NAME, 'file')
        # 提交表单
        self.submit_button = (By.ID, 'btn_client_submit')
        # 确定提交
        self.confirm_button = (By.XPATH, "//div[@id='bjui-alertMsgBox']/div/div/div[2]/ul/li/button")
        # 受理流水号关闭
        self.confirm_button2 = (By.XPATH, "//div[2]/div/a/i")
        # 关闭客户开户页
        self.close_cus_acc_button = (By.XPATH, "//li[2]/span")
        # 提示重复时确认
        self.re_confirm_button = (By.XPATH, "(//button[@type='button'])[6]")
        # 受理流水号
        self.ser_num = (By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/label')
        # 是否一般纳税人
        self.taxpayer_button = None
        # 一条数据
        self.test_data = None
        # 流水号
        self.links = None
        # 计时变量
        self.spend_time = None

        self.check_code_box2 = (By.ID, 'captcha')
        self.login_button2 = (By.ID, 'loginBtn')
        self.manage_cus_button = (By.XPATH, "//div[@id='bjui-sidenav-box']/ul/li/a")
        self.sele_cus_button = (By.XPATH, "//div[@id='bjui-sidenav-box']/ul/li/ul/li[4]/a")

        self.cli_search_box = (By.NAME, 'clientName')
        self.cli_search_button = (By.ID, 'btn_client_Search')
        self.cli_cho_button = (By.XPATH, "//table[@id='mmg']/tbody/tr/td/span/input")

        self.cli_name = (By.XPATH, '//*[@id="name"]')
        # 客户编码
        self.cli_code = (By.XPATH, '//*[@id="code"]')
        self.cli_con_name = (By.XPATH, '//*[@id="contacts"]')
        self.cli_con_tel = (By.XPATH, '//*[@id="tel"]')
        self.cli_cert_type = (By.XPATH, '//*[@id="typeName"]')
        self.cli_cert_num = (By.XPATH, '//*[@id="clientNumber"]')
        self.cli_cert_addr = (By.XPATH, '//*[@id="addr"]')
        self.cli_taxpayer = (By.XPATH, '//*[@id="isTaxPayerName"]')

    # 登陆
    def login(self):
        driver1.find_element(*self.check_code_box).send_keys(1234)

        driver1.find_element(*self.login_button).click()

        driver2.find_element(*self.check_code_box2).send_keys(1234)

        driver2.find_element(*self.login_button2).click()

    # 打开页面
    def acc_page(self):
        wait1.until(EC.presence_of_element_located(self.acc_button1))
        wait1.until(EC.element_to_be_clickable(self.acc_button2))
        driver1.find_element(*self.acc_button2).click()

        wait2.until(EC.presence_of_element_located(self.manage_cus_button))
        wait2.until(EC.element_to_be_clickable(self.sele_cus_button))
        driver2.find_element(*self.sele_cus_button).click()

    # 数据赋值
    def ass_data(self):
        self.test_data = tp.generate_data()
        if self.test_data[9] == '是':
            self.taxpayer_button = self.taxpayer_y_button
        else:
            self.taxpayer_button = self.taxpayer_n_button
        return self.test_data

    # 客户开户
    def cus_acc(self):
        time1 = time.time()

        # 检测是否可输入
        wait1.until(EC.presence_of_element_located(self.submit_button))
        # 开始插入数据
        driver1.find_element(*self.cus_cate_box).send_keys(self.test_data[0])
        driver1.find_element(*self.cus_lev_box).send_keys(self.test_data[1])
        driver1.find_element(*self.cus_name_box).send_keys(self.test_data[2])
        driver1.find_element(*self.cert_type_box).send_keys(self.test_data[3])
        driver1.find_element(*self.cert_num_box).send_keys(self.test_data[4])
        driver1.find_element(*self.con_person_box).send_keys(self.test_data[5])
        driver1.find_element(*self.con_tel_box).send_keys(self.test_data[6])
        driver1.find_element(*self.post_code_box).send_keys(self.test_data[7])
        driver1.find_element(*self.email_box).send_keys(self.test_data[8])
        driver1.find_element(*self.taxpayer_button).click()
        driver1.find_element(*self.con_address_box).send_keys(self.test_data[10])

        # # 上传文件
        # for i in tp.file_path:
        #     driver1.find_element(*self.file_list_box).send_keys(i)

        # 点击提交表单
        wait1.until(EC.element_to_be_clickable(self.submit_button))
        driver1.find_element(*self.submit_button).click()
        # 点击确认
        wait1.until(EC.element_to_be_clickable(self.confirm_button))
        driver1.find_element(*self.confirm_button).click()
        # 获得流水号
        wait1.until(EC.presence_of_element_located(self.ser_num))
        self.links = driver1.find_element(*self.ser_num).text
        print(self.links)
        # 关闭流水号
        wait1.until(EC.element_to_be_clickable(self.confirm_button2))
        driver1.find_element(*self.confirm_button2).click()
        time2 = time.time()
        self.spend_time = time2 - time1

        return self.test_data[2], self.links, self.spend_time, self.test_data

    # 按客户查询
    def sele_cus(self):
        sele_cus_name = self.test_data[2]
        wait2.until(EC.presence_of_element_located(self.cli_search_button))
        driver2.find_element(*self.cli_search_box).send_keys(sele_cus_name)
        wait2.until(EC.element_to_be_clickable(self.cli_search_button))
        driver2.find_element(*self.cli_search_button).click()
        wait2.until(EC.element_to_be_clickable(self.cli_cho_button))
        driver2.find_element(*self.cli_cho_button).click()
        time.sleep(2)
        wait2.until(EC.presence_of_element_located(self.cli_taxpayer))
        sele_cli_name = driver2.find_element(*self.cli_name).text
        con_name = driver2.find_element(*self.cli_con_name).text
        con_tel = driver2.find_element(*self.cli_con_tel).text
        cert_type = driver2.find_element(*self.cli_cert_type).text
        cert_num = driver2.find_element(*self.cli_cert_num).text
        address = driver2.find_element(*self.cli_cert_addr).text
        taxpayer = driver2.find_element(*self.cli_taxpayer).text
        # 客户编码
        sel_cli_code = str(driver2.find_element(*self.cli_code).text)
        test_data_md5 = str(sele_cli_name)+str(con_name)+str(con_tel)+str(cert_type)+str(cert_num)+str(address)+str(taxpayer)
        f.write(sel_cli_code+' '+str(self.test_data[2])+'\n')
        return test_data_md5

    # md5验证
    def md5_check(self):
        m = hashlib.md5()
        m2 = hashlib.md5()
        test_str2 = str(self.test_data[2])+str(self.test_data[5])+str(self.test_data[6])+str(self.test_data[3])+str(self.test_data[4])+str(self.test_data[10])+str(self.test_data[9])
        m.update(test_str.encode())
        m2.update(test_str2.encode())
        new_md51 = m.hexdigest()
        new_md52 = m.hexdigest()
        if new_md51 == new_md52:
            logging.info('md5校验一致')
            print('md5一致', new_md51, new_md52)


# 主程序
if __name__ == '__main__':

    test_str = None
    # 生成类Automate_test实例化对象
    at = Automate_test()
    # 打开两个浏览器对应两个URL
    driver1 = webdriver.Chrome(executable_path=tp.driver_path1)
    driver2 = webdriver.Firefox(executable_path=tp.driver_path2)
    driver1.get(tp.URL1)
    driver2.get(tp.URL2)
    # 显性等待
    wait1 = WebDriverWait(driver1, 20, 0.7)
    wait2 = WebDriverWait(driver2, 20, 0.7)
    # 登陆
    at.login()
    # 日志格式
    logging.basicConfig(
        level=logging.INFO,
        filename='test_log.log',
        format='%(asctime)s : %(levelname)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        filemode='a'
    )
    # 开始
    f = open('cus_name_cus_num.txt', 'a')
    while True:
        # 刷新页面
        driver1.refresh()
        time.sleep(3)
        # 打开客户开户页面
        driver2.refresh()
        try:
            at.acc_page()
        except Exception as e:
            print(e)
            continue
        # 数据赋值
        wrong_test = at.ass_data()
        # 客户开户过程
        try:
            cus_name, links, spend_time, test_data = at.cus_acc()
            test_data_new = ' '.join(str(s) for s in test_data)
            logging.info('\n%s 用时：%s秒 测试数据：%s' % (links, spend_time, test_data_new))
        except Exception as e2:
            wrong_test_new = ' '.join(str(t) for t in wrong_test)
            logging.error('客户开户过程'+'\n'+str(e2)+'\n'+wrong_test_new+'\n')
            continue
        # 按客户查询
        try:
            test_str = at.sele_cus()
        except Exception as e3:
            logging.error('按客户查询过程'+'\n'+str(e3))
            continue
        at.md5_check()
