# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
def solution(N):
    # write your code in Python 2.7
    count = 0
    n = pow(11,N)

    for i in str(n):
        if i == '1':
            count+=1
    print count

def main():
    solution(3)

if __name__ =='__main__':
    main()


# # you can write to stdout for debugging purposes, e.g.
# # print "this is a debug message"
# import math
# def solution(N):
#     # write your code in Python 2.7
#     count = 0
#     size = 2*N
#     tmp_length = 0
#     curr = [[-1]*size]
#     tmp = [[-1]*size]
#     p = []
#
#     for i in range(N):
#         cry = 0
#         curr[0] = -1
#         for j in range(tmp_length):
#             curr[j] = tmp[j] + tmp[j-1] +cry
#             cry = curr[j]/10
#             curr[j] = curr[j] % 10
#
#         if i>0:
#             curr[j] = tmp[j-1] +cry
#             if(curr[j] >=10):
#                 curr[j] = curr[j] %10
#                 j += 1
#                 curr[j] = 1
#             j += 1
#             tmp_length = j
#         else:
#             tmp_length = 1
#
#         p = tmp
#         tmp = curr
#         curr = p
#
#     for i in str(tmp):
#         if i =='1':
#             count += 1
#
#     return count