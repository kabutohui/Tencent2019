# -*- coding: utf-8 -*-


# 最长递增子序列

if __name__ == '__main__':
    values = [10,9,2,5,3,7,101,18]

    longest = {}
    longest[0] = 1
    for i in range(1, len(values)):
        maxlen = -1
        for j in range(0, i):
            if values[i] > values[j] and maxlen < longest[j]:
                maxlen = longest[j]
        if maxlen >= 1:
            longest[i] = maxlen + 1
        else:
            longest[i] = 1

    print(max(longest.values()))
