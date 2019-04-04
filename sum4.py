if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    target = 0

    res, dic = set(), {}
    # get lens
    num_len = len(nums)
    # sorted
    nums.sort()

    for i in range(num_len):
        for j in range(i+1, num_len):
            key = nums[i] + nums[j]
            if key not in dic.keys():
                dic[key] = [(i, j)]
            else:
                dic[key].append((i, j))

    for i in range(num_len):
        for j in range(i+1, num_len-2):
            exp = target - nums[i] - nums[j]
            if exp in dic.keys():
                for tmpindex in dic[exp]:
                    if tmpindex[0] > j:
                        res.add((nums[i], nums[j], nums[tmpindex[0]], nums[tmpindex[1]]))

    print(len(res))