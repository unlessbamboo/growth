# coding:utf8
import heapq
import random


class HeapSorter(object):
    def __init__(self, num_blocks, input_sequence):
        self.num_blocks = num_blocks
        self.input_sequence = input_sequence

    def sorted(self):
        # 堆排序模块heapq.
        # merge: 归并排序
        return heapq.merge(*self.__sorted_subsequences__())

    def __sorted_subsequences__(self):
        """
        构建多个有序列, 每一次yield返回有序列表
        """
        # Initialization: read B pages into the current_heap
        current_heap = [self.input_sequence.pop(0) for x in xrange(self.num_blocks)]
        # 将list(current_heap)变为一个堆结构, 更改原始列表(完全二叉树)
        # 对于下标i元素, 其左右子节点的下标: 2*i+1, 2*i+2
        heapq.heapify(current_heap)
        next_heap = []
        current_run = []

        while current_heap:
            # 首先从堆内存中获取最小值并存入current_run
            lowest = heapq.heappop(current_heap)
            current_run.append(lowest)

            # 其次, 每一次输出之后, 重新获取未排序值放入败者树中
            if self.input_sequence:
                next_element = self.input_sequence.pop(0)
                # 将next_element压入对败者树中, 此时如果next_element小于
                # current_run中的最大值(lowest), 则推入next_heap
                heapq.heappush(current_heap if next_element >= lowest
                               else next_heap, next_element)

            # 每次current_heap为空就表示当前已经构建了一个列表, 并且此时
            # next_heap中的所有值都小于current_run中最大值
            if not current_heap:
                current_heap, next_heap = next_heap, current_heap
                yield current_run
                current_run = []


if __name__ == "__main__":
    # 初始化待排序数值列表
    sorter = HeapSorter(10, [random.randrange(10000) for x in xrange(100)])
    # 排序
    print(list(sorter.sorted()))
