# set of tools required for functional programing
    # modules

# from itertools import count
#
# for i in count(3):
#     print(i)  # will keep on counting until infinity
#     if i >= 20: # to give a stoping point
#         break

from itertools import accumulate, takewhile

numbers = list(accumulate(range(8)))
print(numbers)
print(list(takewhile(lambda x:x <= 6, numbers))) #takewhile takes only certian numbers based on paramerters given
