import datetime
import sys
sys.setrecursionlimit(100000000) #解除默认的999次递归深度限制


def listWrite(list, filename='result.txt'):
    '''
    用于格式化写入的函数
    '''
    with open(filename, 'a') as obj:
        obj.write('{:12} |'.format(list[0]))
        for value in list[1:]:
            if type(value) == int:
                obj.write(' {:^9d} |'.format(value))
            elif type(value) == float:
                if value < 0:
                    obj.write(' {:^7.5f}s |'.format(value))
                else:
                    obj.write(' {:^7.5f}s  |'.format(value))
        obj.write('\n')


def runDecor(func):
    '''
    用于计算运行时间的修饰器
    '''
    def new_func(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return round((end - start), 8)
    return new_func


@runDecor
def PrintN(N):
    '''
    普通Loop实现方法
    '''
    for i in range(1,N+1):
        print(i)

@runDecor
def RePrintN(N):
    '''
    递归实现方法
    '''
    if N:
        RePrintN(N-1)
        print(N)


#以下为运行实现函数
list = ['Times',100,1000,1000] #需要改变次数，请修改此处list
time_nor = ['Loop']
time_rec = ['Recursion']
differ =['Difference']
for value in list[1:]:
    i = 1
    time_nor.append(PrintN(value))
    print("**************Complete {} times normal loop function PrintN **************".format(value))
    time_rec.append(RePrintN(value))
    print("**************Complete {} times recursion function RePrintN**************".format(value))
    differ.append(time_rec[i]-time_nor[i] )

listWrite(list)
listWrite(time_rec)
listWrite(time_nor)
listWrite(differ)





