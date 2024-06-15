# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.
#
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).



                                               # 1st try
# def find_it(seq):
#     count_dict = {}
#
#     # counting all nums
#     for number in seq:
#         if number in count_dict:
#             count_dict[number] += 1
#         else:
#             count_dict[number] = 1
#
#     # looking for num that appears odd numbers of time
#     # dictionaryName.items() returns (key, value) of this dict
#     for number, count in count_dict.items():
#         if count % 2 != 0:
#             return number
#             # only first num that appears odd number of times will be returned


                                                        # 2nd try

# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2 != 0:
#             return i

                                                        # most optimal way to do this
                                                        # using XOR, we are iterating only 1 time
def find_it(seq):
    result = 0
    for number in seq:
        result ^= number
    return result

list = [1,1,2]
print("Integer that appears an odd number in given list is: "+str(find_it(list)))

