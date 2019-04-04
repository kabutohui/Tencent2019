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

def numofBlock(q):
    w, b = 0, 0
    areacount = (q[2] - q[0] + 1) * (q[3] - q[1] + 1)
    if (q[2] - q[0] + 1) % 2 == 0 or (q[3] - q[1] + 1) % 2 == 0: # 如果纵横方向上有偶数，黑白块数一样
        w = int(areacount / 2)
        b = areacount - w
    else:
        # 横纵坐标都为奇数或者偶数的块为白色
        w = len([x for x in range(q[0], q[2]+1) if x % 2 == 0]) * len([x for x in range(q[1], q[3]+1) if x % 2 == 0]) + \
            len([x for x in range(q[0], q[2] + 1) if x % 2 != 0]) * len([x for x in range(q[1], q[3] + 1) if x % 2 != 0])
        b = areacount - w

    return w, b

def countBlock1(filename):
    f = open(filename, 'r')
    T = int(f.readline().strip())
    q = {}
    for i in range(T):
        q['Board'] = [int(i) for i in f.readline().strip().split(' ')]
        q['first'] = [int(i) for i in f.readline().strip().split(' ')]
        q['second'] = [int(i) for i in f.readline().strip().split(' ')]

        # --------- 开始计算 ----------
        # 最开始的白块与黑块的数量
        black = int(q['Board'][0] * q['Board'][1] / 2)
        white = q['Board'][0] * q['Board'][1] - black

        # 两个区域没有重叠
        if max(q['first'][0], q['second'][0]) > min(q['first'][2], q['second'][2]) or  \
                max(q['first'][1], q['second'][1]) > min(q['first'][3], q['second'][3]):
            # 先涂白
            w, b = numofBlock(q['first'])
            # 白色增加的数量，就是该区域中黑色块的数量
            white += b
            black -= b
            # 再涂黑
            w, b = numofBlock(q['second'])
            # 白色减少的数量就是该区域中白色块的数量
            white -= w
            black += w
            print('{0} {1}'.format(white, black))

        else: # 两个区域有重叠
            x_lap = [max(q['first'][0], q['second'][0]), min(q['first'][2], q['second'][2])]
            y_lap = [max(q['first'][1], q['second'][1]), min(q['first'][3], q['second'][3])]
            lap = [x_lap[0], y_lap[0], x_lap[1], y_lap[1]]
            # 先涂白，只管涂白区域减去重叠区域中被涂白的黑色块的数量
            w, b = numofBlock(q['first'])
            w_lap, b_lap = numofBlock(lap)
            white += b - b_lap
            black -= b - b_lap
            # 再涂黑，计算涂黑区域中减少的白色块的数量
            w, b = numofBlock(q['second'])
            white -= w
            black += w
            print('{0} {1}'.format(white, black))

        # --------- 结束计算 ----------

if __name__ == '__main__':
    countBlock1('Task05.txt')