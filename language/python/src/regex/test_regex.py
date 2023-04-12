"""
功能: 正则表达式的使用

9个re模块常量: 
    + IGNORECASE: 忽略大小写匹配, ``re.IGNORECASE``
    + ASCII: ascii码匹配, 简写: ``re.A``
    + DOTALL: DOT表示., dotall就是匹配所有, 默认情况下不匹配``\n``, 此时就可以使用DOTALL, 简写: ``re.S``
    + MULTILINE: 多行模式下匹配, 例如``^var1``就会匹配``h2\nvar123``, 默认情况下不可以, 简写: ``re.M``
    + VERBOSE: 详细模式, 在正则表达式中添加注解, 简写: ``re.X``
    + LOCALE: 由当前语言来决定大小写敏感, ``\w, \B``, 简写: ``re.L``
    + UNICODE: 匹配unicode编码字符, 简写: ``re.U``
    + DEBUG: 显示编译时的信息
    + TEMPLATE: 简写: ``re.T``

12个模块函数:
    a. 查看一个匹配项(3):
        + search: 查找任意未知的匹配项
        + match: 从字符串开头开始匹配
        + fullmatch: 整个字符串和正则完全匹配(很少用)
    b. 查看多个匹配项(2):
        + findall: 从字符串任意位置开始, 返回匹配的数据列表
        + finditer: 从字符串任意位置开始, 返回匹配的数据迭代器
    c. 分割(1):
        + split(ptn, str, maxsplit=0, flags=0): 用ptn分开str, maxsplit表示最大分割次数, flags就是9大常量
    d. 替换(2)
        + sub(ptn, repl, str, count=0, flags=0): 用repl替换str中被ptn匹配的字符, 返回新字符串, 其中repl可为函数
        + subn(ptn, repl, str, count=0, flags=0): 同sub, 但是返回元祖: (字符串, 替换次数)
    e. 编译(2):
        + compile: 将ptn编译为一个正则表达式对象, 加快后续的匹配速度
        + template: 
    f. 其他(2):
        + escape(ptn): 转义正则表达式中具有特殊含义的字符
        + purge(): 清除正则表达式缓存
参考: https://segmentfault.com/a/1190000022242427
"""
import os
import sys
import re


def test_const_var():
    origin = 'bamboo\nHandsome boy, I done not believe'
    pattern = r'^handsom'

    print(f'原始字符串: {repr(origin)}, 匹配: {pattern}')
    print('> 默认模式(无忽略大小写, 无多行), findall结果: ', re.findall(pattern, origin))
    print('> 忽略大小写, 无多行, findall结果: ', re.findall(pattern, origin, re.IGNORECASE|re.MULTILINE))
    print()


class RegexTest:
    """ 正则表达式匹配测试 """

    def regex_test_1(self):
        origin_str, pattern_str = 'hello world', r'hello'
        pattern = re.compile(pattern_str)
        match = pattern.match(origin_str)
        if not match:
            return

        print(f'原始字符串:{origin_str}, 匹配模式:{pattern_str}\n'
              f'\tmatch.group()的值:    {match.group()}\n'
              f'\tmatch.string的值:     {match.string}\n'
              f'\tmatch.re的值:         {match.re}\n'
              f'\tmatch.pos的值:        {match.pos}\n'
              f'\tmatch.endpos的值:     {match.endpos}\n'
              f'\tmatch.start()的值:    {match.start()}\n'
              f'\tmatch.end()的值:      {match.end()}\n')
        print("======================================")

    def regex_test_2(self):
        # \w匹配单词字符
        p = re.compile(r'(\w+) (\w+)')
        s = 'i say, hello world!'

        print(p.sub(r'\2 \1', s))

        def func(m):
            return m.group(1).title() + '(function)' + m.group(2).title()

        print(p.sub(func, s))
        print("======================================")


def test_re_func():
    # 1. search, 返回值可以通过g.start, g.end进行位置索引, 仅仅查找一个
    origin = 'aBamboo帅哥x, Bamboo帅, 媛美女-x'
    ptn = r'Bamboo帅'
    print(f'原始:{origin}, ptn:{ptn}, search结果: {re.search(ptn, origin).group()}')
    print()

    # 2. match, 从字符串开头就开始匹配, 仅仅查找一个
    print(f'原始:{origin}, ptn:{ptn}, match结果: {re.match(ptn, origin)}')
    print()


if __name__ == "__main__":
    print('--------测试匹配成功后match中的属性--------')
    regexTest = RegexTest()
    regexTest.regex_test_1()
    regexTest.regex_test_2()
    print()

    print('--------测试re九大常量--------')
    test_const_var()
    print()

    print('--------测试re函数--------')
    test_re_func()
    print()
