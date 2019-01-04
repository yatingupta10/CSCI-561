# from itertools import permutations 
# import itertools
# l = list(permutations([1, 0, 0, 1])) 
# # l = list(l for l,_ in itertools.groupby(l))
# l = list(set(l))
# print l 
# # print type(l[0])

# def get_all_sub_mat(mat):
#     rows = len(mat)
#     cols = len(mat[0])
#     def ContinSubSeq(lst):
#         size=len(lst)
#         for start in range(size):
#             for end in range(start+1,size+1):
#                 yield (start,end)
#     for start_row,end_row in ContinSubSeq(list(range(rows))):
#         for start_col,end_col in ContinSubSeq(list(range(cols))):
#             yield [i[start_col:end_col] for i in mat[start_row:end_row] ]
import time

start_time = time.clock()
# Matrix = [(0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0), (0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0)]
Matrix = [[1,1,1,1,0,0,0], [0,0,0,0,1,0,1], [0,0,0,0,1,1,0], [0,0,0,0,0,0,1]]
print len(Matrix)
# print next(y)

def ContinSubSeq(lst):
  size=len(lst)
  for start in range(size):
    for end in range(start+1,size+1):
      yield (start,end)

def getsubmat(mat,start_row,end_row):
  return [i[:] for i in mat[start_row:end_row] ]

def get_all_sub_mat(mat):
  rows = len(mat)
  cols = 7
  for start_row,end_row in ContinSubSeq(list(range(rows))):
  	print str(start, end)
    # for start_col,end_col in ContinSubSeq(list(range(cols))):
    yield getsubmat(mat,start_row,end_row)

for i in get_all_sub_mat(Matrix):
  print i

# def all_sub(r, c, mat): # returns all sub matrices of order r * c in mat
#     arr_of_subs = []
#     if (r == len(mat)) and (c == len(mat[0])):
#             arr_of_subs.append(mat)
#             return arr_of_subs
#     for i in range(len(mat) - r + 1):
#         for j in range(len(mat[0]) - c + 1):
#         	print j
#         	temp_mat = []
#         	for ki in range(i, r + i):
#         		temp_row = []
#         		for kj in range(j, c + j):
#         			temp_row.append(mat[ki][:])
#         		temp_mat.append(temp_row)
#         	arr_of_subs.append(temp_mat)
#     return arr_of_subs
# for i in all_sub(3, 7, Matrix):
# 	print i
print time.clock() - start_time, "seconds"
print len(Matrix)
# [(0, 0, 1, 0, 1, 0, 1), (0, 1, 0, 1, 1, 0, 0), (0, 1, 0, 0, 1, 0, 1), (1, 1, 0, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1), (1, 0, 0, 0, 1, 1, 0), (1, 0, 1, 1, 0, 0, 0), (0, 0, 1, 1, 0, 0, 1), (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 1, 0, 0, 1), (0, 1, 0, 0, 1, 1, 0), (0, 1, 1, 0, 0, 1, 0), (1, 1, 0, 0, 1, 0, 0), (1, 0, 0, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0, 0), (0, 0, 1, 1, 0, 1, 0), (0, 1, 0, 1, 0, 1, 0), (0, 1, 1, 0, 1, 0, 0), (1, 0, 0, 0, 0, 1, 1), (1, 0, 1, 0, 0, 0, 1), (0, 0, 1, 0, 0, 1, 1), (0, 1, 1, 1, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1), (0, 0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0, 1), (1, 1, 0, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 1, 1, 0), (1, 0, 0, 1, 1, 0, 0), (1, 0, 0, 0, 1, 0, 1), (1, 1, 0, 0, 0, 0, 1), (0, 0, 1, 1, 1, 0, 0)]
