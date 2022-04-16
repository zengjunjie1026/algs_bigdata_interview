
# [(1, 2), (1, 3), (1, 5), (2, 4), (3, 6), (9, 11), (9, 16), (12, 17)]

def merge(intervals):
    if intervals ==[]:

        return []
    intervals = sorted(intervals, key=lambda x:x[0])    #对输入的intervals进行排序
    invalNow = intervals[0]  # (min.max)
    result = []
    for i in range (1,len(intervals)):
        if(invalNow[1]>=intervals[i][0]):  # 只要上一个区间右边（较大）的值大于或等于下一个区间左边（较小）的值
            invalNow[1] = max(invalNow[1],intervals[i][1])
        else:
            result.append(invalNow)
            invalNow=intervals[i]
    result.append(invalNow)
    return result


def merge2(intervals):
    res = []
    intervals.sort()
    for i in intervals:
        if not res or res[-1][1]<i[0]:
            res.append(i)
        else:
            res[-1][1] = max(res[-1][1],i[1])
    return res


if __name__ == '__main__':

    data = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(data))

