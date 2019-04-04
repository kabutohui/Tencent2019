# -*- coding: utf-8 -*-

# 在一场比赛中有n个检查点，比赛要求到达n-1个检查点即可，这些检查点排列在x轴上，
# 位置分别为x1，x2，...，xn，且允许以任意顺序访问检查点。比赛的开始位置为a，
# 求完成比赛所经过的最小距离。
#
# 【输入描述：】
# 输入包含两行
# 第一行为两个参数n，a，其中1 <= n <= 100000, -1000000 <= a <= 1000000
# 第二行为n个整数：x1,x2,...,xn(-1000000 <= xn <= 1000000)
#
# 【输出描述】
# 输出一个整数
#
# 输入：
# 3 10
# 1 7 12
#
# 输出：
# 7

def minDistance(l1, l2):

    n, x0 = l1[0], l1[1]
    point = l2

    point_sorted = sorted(point)

    if x0 < point_sorted[0]:
        return point_sorted[-2] - x0
    elif x0 > point_sorted[-1]:
        return x0 - point_sorted[1]
    else:
        # 判断x0与左右两个端点之间的距离
        l = x0 - point_sorted[0]
        r = point_sorted[-1] - x0
        if l > r: # 如果左边大于右边，则去掉第一个值
            return min(r, x0 - point_sorted[1]) + point_sorted[-1] - point_sorted[1]
        else:
            return min(l, point_sorted[-2] - x0) + point_sorted[-2] - point_sorted[0]


if __name__ == '__main__':
    test1 = {'l1': [3, 10], 'l2': [1, 7, 12], 'result': 7}
    test2 = {'l1': [3, 14], 'l2': [1, 7, 12], 'result': 7}
    test3 = {'l1': [3, 0], 'l2': [1, 7, 12], 'result': 7}

    test = [test1, test2, test3]

    count = 0

    for t in test:
        if minDistance(t['l1'], t['l2']) == t['result']:
            count += 1
        else:
            print('l1:', t['l1'], '\nl2:', t['l2'], '\nOutput:', minDistance(t['l1'], t['l2']), '\nExpect:', t['result'])

    print('Case通过率：', count*100 / len(test), '%')

