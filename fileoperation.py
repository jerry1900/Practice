import os


def read_file(filename):
    f = open(filename, 'r+')
    print(f.read())
    f.close()


def write_file():
    f = open('test.txt', 'a+')
    f.write('my name is jerry')
    f.close()


def read_and_write():
    f1 = open('test.txt', 'r')
    text = f1.read()
    print(text)
    f2 = open('write_to.txt', 'w+')
    f2.write(text)
    # f2.seek(0)
    #  此时文件的写入已经成功了，但是文件指针还在文件末尾，所以此时如果去读，是什么也读不出来的
    #  只有将文件指针调至开头，才能读出来东西
    print(f2.read())
    f1.close()
    f2.close()

def try_with():
    with open('write_to.txt', 'a') as f:
        f.write('\nnew message')

try_with()
read_file('write_to.txt')

# read_and_write()

