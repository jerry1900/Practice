try:
    result = float(input('请输入分子:\n'))/float(input('请输入分母:'))
    print(result)

except ValueError:
    print('必须输入数字')
except ArithmeticError:
    print('分母不能为零')

else:
    print('代码继续执行')

finally:
    print('无论是否异常，都必须执行这里')
