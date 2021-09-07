# 変数定義
# correct
x = 1
y = 1
# wrong
xxxx     = 1
y        = 1

x = 1

# 関数の引数の「=」にはスペース不要
# correct
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# wrong
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

# operatorの周りにスペース一個, operatorにpriorityがある場合はスペースをなくす
# correct
x = x + 1
x += 1
x = x*2 - 1
a = x*x + y*y
c = (a+1) * (a-1)

# wrong
x=x+1
x +=1
x = x * 2 - 1
a = x * x + y * y
c = (a + 1) * (a - 1)

# カンマの後にはスペースを入れる
# correct
range(1, 11)
a = [1, 2, 3, 4]
b = (1, 2, 3, 4)

# wrong
range(1,11)
a = [1,2,3,4]
b = (1,2,3,4)

# カンマの後に閉じカッコが来る場合はスペースは不要
# correct
foo = (0,)

# wrong
foo = (0, )


# correct
FILES = [
    'setup.cfg',
    'tox.ini',
]

# wrong
FILES = ['setup.cfg', 'tox.ini',]

# 行の折り返し
# correct
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# wrong
foo = long_function_name(var_one, var_two,
    var_three, var_four)


# correct
def long_function_name(
        var_one, var_two, var_three, var_four):
    print(var_one)

def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# wrong
def long_function_name(
    var_one, var_two, var_three, var_four):
    print(var_one)

def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

# '\'で区切って改行する
print("このように表示する文章が長かったりする場合は\
バックスラッシュで区切ると改行できます。")

#correct
a = 1000000000000000000000000000 \
    + 1000000000000000000 \
    + 10000000000000000000000000\
    + 100000000 \
    + 100000

# wrong
a = 1000000000000000000000000000 +\
    10000000000000000000 +\
    100000000 +\
    10000000000000

# 関数間は二行空ける
def func():
    pass


def func2():
    pass

# 同じクラス内では一行
class MyClass:
    def __init__(self):
        pass

    def method(self):
        pass

#importのStyle
#correct
import os
import sys

from subprocess import Popen, PIPE

# wrong
import os, sys

# 順番
# 1. Standard library (time, sys)
# 2. Third party (numpy, pandas)
# 3. Our library
# 4. Local library
# それぞれ一行空ける (abc順)

# absolute import
import mypkg.sibling
from mypkg import sibling
from mypkg sibling import example

from package.subpackage1.subpackage2.subpackage3.module4 import function