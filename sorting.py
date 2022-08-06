# take a list
# take one element from the list and start comparing from that element, swap if the first element is greater than second element, otherwise continue
# for taking one element from a list ,we need one for loop
# for comparing the element throughout the element, we need one more loop.
l = [5, 3, 9, 12, 1]
# take 5 and compare 5 with 3, 5 > 3, so we need to swap, [3, 5, 9, 12, 1]
# take same element 5 and compare with next element, 5 < 9, so no need to swap, [3, 5, 9, 12, 1]
# take same element 5 and compare with 1, 5 > 1, so we need to swap, [3, 1, 9, 12, 5]
# 3 > 1 , [1, 3, 9, 12, 5]
# 3 < 9, [1, 3,9,12,5]
# 3 < 12, [1,3,9,12,5]
# 3 < 5, [1,3,9,12,5]
# 9 < 12, [1,3,9,12,5]
# 9>5, [1,3,5,12,9]
# 12>9,[1,3,5,9,12]
# def sorting(l):
#     for i in range(len(l)):
#         for j in range(i+1, len(l)):
#             if l[i] > l[j]:
#                 l[i], l[j] = l[j], l[i]
#     return l
#
# print(sorting([22.6,11,9,1,1000,34]))
for i in range(4):
    for j in range(4):
        if i == j:
            print('')
        else:
            print('*', end=' ')
        # else:
        #     print(' ', end=' ')
    print()
