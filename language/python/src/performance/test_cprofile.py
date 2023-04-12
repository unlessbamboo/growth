"""
使用cProfile进行性能测试

输出和说明:
     ncalls  tottime  percall  cumtime  percall     filename:lineno(function)
      2        0.028    0.014    0.028    0.014     test_cprofile.py:8(sum_num)

    + ncalls: 调用次数
    + tottime: total time, 总运行时间, 不包括子函数运行时间
    + percall: per-call, 值计算: tottime/ncalls
    + cumtime: 函数开始调用到返回的时间
    + percall: cumtime/ncalls
    + filename: 函数相关信息

参考: https://juejin.cn/post/7065935111652540453
"""
import pstats
import cProfile


def sum_num(max_num):
    """sum_num:累加

    :param max_num:最大值
    """
    total = 0
    for i in range(max_num):
        total += i
    return total


def test():
    """test"""
    total = 0
    for i in range(40000):
        total += i

    t1 = sum_num(100000)
    print("次数{0}，测试结束.".format(t1))
    t2 = sum_num(400000)
    print("次数{0}，测试结束.".format(t2))


if __name__ == "__main__":
    '''Use cProfile module test program performance.'''
    # 所有的性能统计结果都会记录到result.out中
    print('-------------begin----------------')
    cProfile.run('test()', filename="result.out")
    print()

    print('-------------analysis from filename----------------')
    pstats.Stats('result.out').sort_stats('time').print_stats()
    print()
