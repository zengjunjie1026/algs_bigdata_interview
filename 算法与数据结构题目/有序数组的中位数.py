# def median(A, B):
#     # m ,n为两个数组的长度
#     m, n = len(A), len(B)
#     if m > n:
#         A, B, m, n = B, A, n, m
#     # n是较大的那个数组的长度
#     if n == 0:
#         raise ValueError
#
#     # [0, m]区间进行查找
#     imin, imax = 0, m
#     # 假设 i+j = m-i + n-j
#     # 如果n>=m了就说明n数组比m数组长 那就在n-j那一部分+1  于是： i+j = m-i + n-j+1
#     # 于是化简得到 j = ((m+n+1)/2) - i
#     half_len = int((m + n + 1) / 2)  # 注意要整形,不然没办法查找 注意int(5/2)=2
#     while imin <= imax:
#         i = int((imin + imax) / 2)
#         j = half_len - i
#         # i>m right就为负了
#         if i < m and B[j - 1] > A[i]:
#             # 说明A[i]太小了
#             imin = i + 1
#         # i<0 更不可能...
#         elif i > 0 and A[i - 1] > B[j]:
#             # 说明A[i-1]太大了
#             imax = i - 1
#         else:
#             # 这个时候第一个条件就完成了 进入到第二个条件
#             # 极限思想去考虑边界情况
#             if i == 0:
#                 max_of_left = B[j - 1]
#             elif j == 0:
#                 max_of_left = A[i - 1]
#             # 这个是一般情况 二选一
#             else:
#                 max_of_left = max(A[i - 1], B[j - 1])
#             # 如果是奇数的话 直接返回就行了
#             if (m + n) % 2 == 1:
#                 return max_of_left
#             # 偶数的话右边也要算
#             if i == m:
#                 min_of_right = B[j]
#             elif j == n:
#                 min_of_right = A[i]
#             else:
#                 min_of_right = min(A[i], B[j])
#
#             return (max_of_left + min_of_right) / 2.0
#
#
# if __name__ == '__main__':
#     A = [1, 2]
#     B = [3, 4]
#     ans = median(A, B)
#     print(ans)

def median_4(A, B):
    # 思路四:二分法, i = 0 ~ m, j = (m + n + 1) / 2 - i, 需保证j>=0, 即n>=m
    # 时间复杂度: O(log(min(m,n)))
    m, n = len(A), len(B)
    if m > n:
        m, n, A, B = n, m, B, A
    if n == 0:
        raise ValueError
    i_min = 0
    i_max = m
    
    #中间的数
    half = (m + n + 1) // 2
    
    # 二分法
    while i_min <= i_max:
        i = (i_min + i_max) // 2
        j = half - i
        
        # a[mid] > B[mid]
        if i > 0 and A[i - 1] > B[j]:
            # i太大了
            i_max = i - 1
        
        #a[mid]  < b[mid]
        elif i < m and A[i] < B[j - 1]:
            # i太小了
            i_min = i + 1
        
        else:
            if i == 0:
                max_of_left = B[half - 1]
            elif j == 0:
                max_of_left = A[half - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])
            if (m + n) % 2 == 1:
                return max_of_left
            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])
            return (max_of_left + min_of_right) / 2


print(median_4([1,2,3,4],[3,4,5,67]))
