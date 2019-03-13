# -*- coding: utf-8 -*-

# 一棋盘共有n行m列，任意相邻的两个格子都是不同色（黑或白），坐标（1,1）的格子为白色。
# 已知n和m，条件如下两步，求黑白方块的数量:
# 第一步：在这块棋盘里选择一个左下角坐标（x0，y0），右上角坐标为（x1，y1），把（x1-x0+1）*（y1-y0+1）的方块涂白。
# 第二步：在这块棋盘里选择一个左下角坐标（x2，y2），右上角坐标为（x3，y3），把（x3-x2+1）*（y3-y2+1）的方块涂黑。
#
# 输入描述：
# 第一行一个整数T，表示提问T次。
# 接下来3*T行
# 第（1+3*i）行两个整数n，m，表示d第i次提问棋盘大小。
# 第（2+3*i）行四个整数x0，y0，x1，y1，表示第i次提问涂白操作的两个坐标。
# 第（3+3*i）行四个整数x2，y2，x3，y3，表示第i次提问涂黑操作的两个坐标。
# i<=T<=10000，1<=x<=n<=1000000000,1<=y<=m<=1000000000,x0<=x1,y0<=y1,x2<=x3,y2<=y3；
#
# 输出表示：
# 共T行，每行两个整数分别表示白色和黑色方块的数量。
#
# 示例：
# 输入
# 3
# 1 3
# 1 1 1 3
# 1 1 1 3
# 3 3
# 1 1 2 3
# 2 1 3 3
# 3 4
# 2 1 2 4
# 1 2 3 3
#
# 输出：
# 0 3
# 3 6
# 4 8

import numpy as np

def countBlock(filename):
    f = open(filename, 'r')
    T = int(f.readline().strip())
    q = {}
    for i in range(T):
        q['Board'] = [int(i) for i in f.readline().strip().split(' ')]
        q['first'] = [int(i) for i in f.readline().strip().split(' ')]
        q['second'] = [int(i) for i in f.readline().strip().split(' ')]

        # --------- 开始计算 ----------
        # 最开始的白块与黑块的数量
        board = np.array([i % 2 for i in range(q['Board'][0] * q['Board'][1])]).reshape(q['Board'][0], q['Board'][1])
        board[q['first'][0]-1: q['first'][2], q['first'][1]-1: q['first'][3]] = 0
        board[q['second'][0]-1: q['second'][2], q['second'][1]-1: q['second'][3]] = 1

        print("{0} {1}".format(q['Board'][0] * q['Board'][1] - board.sum(), board.sum()))
        # --------- 结束计算 ----------

if __name__ == '__main__':
    countBlock('Task05.txt')