import pytest
"""
一、使用fixture函数需要两步
1、定义fixture函数
2、如何调用
二、Python三大器
生成器 包含yield  生成器就是特殊的迭代器，特点：边计算边遍历，节省内存，有记忆功能
迭代器  能用for ..in..循环遍历的  自己写迭代器必须含：__next__,__iter__这两个方法的
装饰器：带@符号，作用：在不改变原来函数功能的前提下，增加额外的功能，体现代码的复用性
"""
# 调用方式一：默认方式
# 定义
# 作用域：默认scope是函数级别
@pytest.fixture
def login():
    print('输入账号，密码，登录')
    # 可以传返回值
    # return 100
    # yield运行方式 :1、销毁函数返回值-初始化的时候执行  2、yield 100之后就执行作用域范围的测试用例
    # 3、作用范围的测试用例结束之后，开始执行print('要进行清场了')
    yield 100
    print('要进行清场了')


# 使用fixture
# 1、直接把被装饰的函数的名字直接当作参数传入测试用例里面
def test_1(login):
    print('用例1：登录之后，点击购物车')
    print(login)


def test_2(login):
    print('用例2：登录之后，点击修改个人资料')


# 调用方式二：调用不同的函数
@pytest.mark.usefixtures('login')
def test_3(login):
    print('登录之后，点击修改地址')


# # 调用方式三：写参数
# @pytest.fixture(scope='function', autouse='True')
# def test_4():
#     print('用例4，登录之后，点击保存')



