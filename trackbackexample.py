import traceback


class SelfException(Exception):
    pass


def main():
    method1()


def method1():
    method2()


def method2():
    method3()


def method3():
    raise SelfException('Self Defined Exception')


try:
    main()

except:
    traceback.print_exc()
    # traceback.print_exception()
