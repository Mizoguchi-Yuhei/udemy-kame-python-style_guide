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