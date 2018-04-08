import random
import time
import string
# 用户页面
URL1 = 'http://192.168.1.241:9016/businessAccept/login'
# 管理页面
URL2 = 'http://192.168.1.241:9016/businessManagement/login'
# 谷歌浏览器驱动路径
driver_path1 = '/Users/james/PycharmProjects/test_baidu/chromedriver'
# 火狐浏览器驱动路径
driver_path2 = '/Users/james/PycharmProjects/test_baidu/geckodriver'

# 客户开户模块上传文件路径
file_path = [
    '/Users/james/Desktop/testfile/aa.txt',
    '/Users/james/Desktop/testfile/aacopy2.txt',
    '/Users/james/Desktop/testfile/aacopy3.txt',
    '/Users/james/Desktop/testfile/aacopy4.txt',
    '/Users/james/Desktop/testfile/aacopy5.txt',
    '/Users/james/Desktop/testfile/aacopy6.txt',
    '/Users/james/Desktop/testfile/aacopy7.txt',
    '/Users/james/Desktop/testfile/aacopy8.txt',
    '/Users/james/Desktop/testfile/aacopy9.txt',
    '/Users/james/Desktop/testfile/aacopy10.txt'
]

# 客户类型
customer_cate = ['企业', '个人']
# 客户级别
customer_lev = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 证件类别
cert_types = ['身份证', '企业营业执照号']
# 是否一般纳税人
gen_taxpayers = ['是', '否']
# 邮箱后缀
email_sufs = ['@163.com', '@qq.com', '@sina.com', '@sohu.com', '@yahoo.com']


# 随机生成规则内数据
def generate_data():
    # 随机客户类型
    cus_cate = random.sample(customer_cate, 1)[0]
    # 随机客户级别
    cus_lev = random.sample(customer_lev, 1)[0]
    # 时间戳加随机客户名称
    lt = time.localtime()
    lt2 = time.strftime('%y%m%d%H%M%S', lt)
    nl = []
    for i in range(0, random.randint(1, 8)):
        val = random.randint(0x4e00, 0x9fbf)
        nl.append(chr(val))
    nl2 = ''.join(nl)
    cus_name = nl2 + lt2
    # 随机证件类型
    cert_type = random.sample(cert_types, 1)[0]
    # 随机证件号码
    cert_num = random.randint(0, 100000000000000000000)
    # 随机联系人
    cnl = []
    for i in range(0, random.randint(1, 20)):
        val2 = random.randint(0x4e00, 0x9fbf)
        cnl.append(chr(val2))
    cnl2 = ''.join(cnl)
    # 随机联系电话
    con_tel = random.randint(0, 100000000000)
    # 随机邮政编码
    post_num = random.randint(0, 100000)
    # 随机邮箱
    src_digits = string.digits
    src_letter = string.ascii_lowercase
    email_sufs = ['@163.com', '@qq.com', '@sina.com', '@sohu.com', '@yahoo.com']
    num = random.randint(1, 30)
    digits_num = random.randint(1, num)
    letter_num = random.randint(0, (num - digits_num))
    email_num = []
    for i in range(digits_num):
        email_num += random.sample(src_digits, 1)[0]
    email_letter = []
    for i in range(letter_num):
        email_letter += random.sample(src_letter, 1)[0]
    email_pre = email_num + email_letter
    email_suf = random.sample(email_sufs, 1)[0]
    # 打乱字符串
    random.shuffle(email_pre)
    # 列表转字符串
    new_email_pre = ''.join(email_pre)
    email = new_email_pre + email_suf
    # 随机是否一般纳税人
    gen_taxpayer = random.sample(gen_taxpayers, 1)[0]
    # 随机联系地址
    addrl = []
    for i in range(0, random.randint(1, 100)):
        val3 = random.randint(0x4e00, 0x9fbf)
        addrl.append(chr(val3))
    address = ''.join(addrl)
    # 生成这条数据
    data = [cus_cate, cus_lev, cus_name, cert_type, cert_num, cnl2, con_tel, post_num, email, gen_taxpayer, address]
    # print(data)
    return data