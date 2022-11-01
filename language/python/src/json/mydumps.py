# coding:utf8
"""
实现类似json.dumps(obj, indent=2)的功能
"""
from __future__ import print_function


def dump(obj, indent=2, islast=False):
    spacing = ' '
    if isinstance(obj, dict):
        print('%s{' % ((indent) * spacing))
        obj_len = len(obj)
        for index, k in enumerate(obj):
            #  print(index, '--', index)
            v = obj[k]
            if isinstance(v, (list, dict)):
                print('%s"%s":' % ((indent + 1) * spacing, k))
                dump(v, indent + 1, index == (obj_len - 1))
            elif index != (obj_len - 1):
                print('%s"%s": %s,' % ((indent + 1) * spacing, k, v))
            else:
                print('%s"%s": %s' % ((indent + 1) * spacing, k, v))
        print('%s}' % (indent * spacing), end='')
    elif isinstance(obj, list):
        print('%s[' % ((indent) * spacing))
        for index, v in enumerate(obj):
            if isinstance(v, (list, dict)):
                dump(v, indent + 1)
            else:
                print('%s%s' % ((indent + 1) * spacing, v))
        print('%s]' % ((indent) * spacing), end='')
    else:
        print('%s%s' % (indent * spacing, obj), end='')

    print(',') if not islast else print('')


if __name__ == '__main__':
    dump({'kuang': 3, 'edus': [{'name': 'H1', 'location': 3}, {
         'name': 'H2', 'location': 4}], 'age': 100}, islast=True)
