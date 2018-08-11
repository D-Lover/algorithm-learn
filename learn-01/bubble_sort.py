'''
    author：Alive
    date: 2018-08-11 16:35
    desc: 冒泡排序
'''
class BubbleSort(object):

    # 外层循环长度-1
    # 里层循环外层的长度
    def sort(self, arr):
        if not (len(arr)):
            return
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if (arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [10, 0, 100, 98, 14, 78]

s = BubbleSort()
s.sort(arr)

print(arr)
