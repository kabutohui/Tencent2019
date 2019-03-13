# -*- coding: utf-8 -*-

# 小Q得到了一个长度为n的序列A，A中的数各不相同。对于A中的每一个数Aj，
# 求：min(1 <= j < i)|Ai - Aj|，令这个式子取到的最小值的j记为Pi，
# 若最小值不唯一，则选择使Aj较小的那个。
#
# 【输入描述】
# 第一行一个整数n(n <= 10^5)
# 第二行n个整数A1，A2，...，An(|An| <= 10^9)
#
#
# 【输出描述】
# n-1行，每行两个整数用空格隔开。分别表示当i取2~n的时候，对应的min(1 <= j < i)|Ai - Aj|和Pi
#
# 输入：
# 3
# 1 5 3
#
# 输出：
# 4 1
# 2 1

def printResults(n, A):

    for i in range(2, n+1):
        pi = 0
        minval = 10**9
        for j in range(1, i):
            if minval > abs(A[i-1] - A[j-1]):
                minval = abs(A[i-1] - A[j-1])
                pi = j
            elif minval == abs(A[i-1] - A[j-1]):
                if A[pi-1] > A[j-1]:
                    pi = j
        print('{0} {1}'.format(minval, pi))

if __name__ == '__main__':
    n = 4
    A = [1, 5, 3, 4]
    printResults(n, A)

