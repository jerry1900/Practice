# This is a sample Python script.
import random
import test

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #     print('''my name is "jerry wan"
    # i want to learn python
    # everyday''')
    #     print(type(name))
    #     print(True + 1)
    #     print(False + 3)
    #     a = input("Input number 1:")
    #     b = input("Input number 2:")
    #     c = "I will help you to add them up"
    #
    #     print(a,type(a))
    #     print(b,type(b))
    #
    #     print(c)
    #     print(int(a)+int(b))
    #     print('jerry','is','a boy',sep='*',end='')
    #     print('jenny', 'is', 'a girl',sep='$')
    #     x = True
    #     y = False
    #     x ^= y
    #     print(str(x))
    #     a = 100
    #     b = 80
    #     max = a if a > b else b
    #     print(str(max))
    #     a = 10
    #     b = 20
    #     c = 30
    #     max = a if a > b else b if b > c else c
    #     print(max)
    #     aList = ['jerry', 1, [2, 3], 4.0, 1]
    #     del aList[0:2]
    #     print('1这个数字出现了%s次'%aList.count(1))
    #     l1 = [1, 2, 3, 4, 5]
    #     l2 = l1
    #     # del l1[:]
    #     print(l1,id(l1))
    #     print('第一个元素是%s'%l2[0])
    #     a = {'one': 1, 'two': 2, 'three': 3}
    #     b = dict(one=1, two=2, three=3)
    #     # x = a.setdefault('three',4)
    #     x = a.update({'one': 11})
    #     print(x)
    #     print(a)
    #     a = {1,2,3,4}
    #     b = {2,3,4,5,6}
    #     c = b - a
    #     print(c)
    number = random.randint(1, 100)
    guess = int(input('请输入一个1到100之间的数字：'))

    while guess != number:
        if guess > number:
            guess = int(input('你猜的数太大啦，请输入一个小于%d的值：' % guess))

        else:
            guess = int(input('你猜的数太小啦，请输入一个大于%d的值：' % guess))

    print('恭喜你猜对啦~')


# Press the green button in the gutter to run the script.
def print_loop():
    str_name = 'i am jerry wan'
    i = 0
    while i < len(str_name):
        print(str_name[i], end='')
        i += 1


def bubble_algorithm():
    new_list = [3, 4, 5, 6, 3, 1, 2, 9, 1, 2]
    length_of_list = len(new_list)

    # 进入一个执行n-1次的外循环
    i = 0
    while i < length_of_list - 1:
        # 进入一个执行n-1次的内循环

        j = 0
        while j < length_of_list - 1 - i:
            # 比较前后两个元素大小，如果前者大，就把前置的值赋给后者，后者的值赋给前者
            if new_list[j] > new_list[j + 1]:
                bigger_one = new_list[j]
                new_list[j] = new_list[j + 1]
                new_list[j + 1] = bigger_one

            j += 1

        i += 1


    else:
        print('排序完成，输出排序后的数组')
        for e in new_list:
            print(e)


def calculate_annual_rate():
    # 请求用户输入初始本金
    initial_money = input('请输入初始本金,请输入数字：')
    # 请求用户输入期末金额
    accumulated_money = input('请输入期末本金,请输入数字：')
    # 请输入投资年限
    invest_year = input('请输入持有年限,请输入数字：')

    annual_return_rate = (float(accumulated_money) / float(initial_money)) ** (1 / float(invest_year)) - 1

    print('The annual return rate is:{:.3%}'.format(annual_return_rate))


def calculate_final_value():
    # 请求用户输入初始本金
    initial_money = input('请输入初始本金,请输入数字：')
    # 请输入投资年限
    invest_year = input('请输入持有年限,请输入数字：')
    # 请输入年复合收益率
    annual_return_rate = input('请输入年复合收益率:')

    final_value = ((1 + float(annual_return_rate) / 100) ** float(invest_year)) * float(initial_money)

    print('The final value of the investment is {:,f}'.format(final_value))


# 演示如何进行逆向收集参数
def accept_args(name, age):
    print(name)
    print(age)


if __name__ == '__main__':
    # print_hi('PyCharm')
    # calculate_annual_rate()
    calculate_final_value()


# See PyCharm help at https:/
# /www.jetbrains.com/help/pycharm/
