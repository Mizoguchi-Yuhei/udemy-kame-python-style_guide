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

# コメント
# ・コメントは常に最新にする。コメントとコードの中身が異なるなら、コメントは無い方がまし
# ・なるべく英語で書く。絶対に日本語がわからない人が読まないなら日本語でもOK
# ・書くときは文章で書くのが望ましい
# ・# のあとに半角スペースを入れる
# ・インラインコメントはコードの後に半角スペースを2つ入れて#を書く
# ・Docstringは基本的に全てのmodule, function, class, methodにつける(non publicな外からアクセスしない関数には不要)
# ・そのコードが「なにをしているか」より「なぜそう書いたのか」の方が有益

# 命名規則(naming convention)
# 変数名や関数(メソッド)名： snake_case 例) balance, image_height
# クラス名: CamelCase 例) Person, MyClass
# モジュール名やパッケージ名: なるべく短いlower caseで、必要であればsnake_case 例) time, numpy
#
# アンダースコア
# - _xxx: internal use only(non public)の意味
# - xxx_: Pythonですでに使われている単語を使いたいとき 例) type_
# - __xxx: クラスの属性として使うことで名前修飾される
# - __xxx__: magic methodと呼ばれるもので、Pythonが特別に設定しているもの。開発者定義することはない。(overrideすることはある)
# - _:最近実行した戻り値や、iteration時に使われない変数

for _ in range(10):
    print("hello")

l, I, 1, 0, o 一文字の変数は1や0に見間違えるので使わない
# correct
length = len(letter)
# wrong
l = len(letter)

# Constants(宣言後変更しない変数)は大文字のsnakecaseを使う
PI = 3.14
# PI = 3