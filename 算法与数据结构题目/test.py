def getLongStr(a):
    """滑动窗口"""
    lenght = len(a)
    s = set()
    ans = i = j = 0
    while i < lenght and j < lenght:
        if a[j] not in s:
            s.add(a[j])
            j += 1
            ans = max(ans, j-i)
        else:
            s.remove(a[i])
            i += 1
    return ans


if __name__ == "__main__":
    a = getLongStr("abbbchuehuid")
    print(a)