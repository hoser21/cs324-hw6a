# Authors: Kevin Hoser and Alex Schendel
# Date: 03/21/2020
# CS 324

# Problem: Given a list of positive integers, can the set be partitioned into two subsets that
#          the sums of the elements in each subset are the same.

### Helper functions

# return true if the array contains a negative int, else false
def has_neg_int(arr):
    for i in arr:
        if i < 0:
            return True
    return False

### Recursive implenetation
def eq_subsets(L):
    if has_neg_int(L):
        return False
    
    #  if the sum of the array is odd, return false
    if sum(L) % 2 != 0:
        return False
    
    return eq_subsets_r(L, len(L), sum(L)/2)


# return true if we can find N items in L that sum up to S
def eq_subsets_r(L, N, S):
    if S == 0:
        return True
    
    if N == 0 and S > 0:
        return False

    
    pass


### Dynamic implementation
def eq_subsets_dp(L):
    if has_neg_int(L):
        return False
    pass


if __name__ == '__main__':
    test_arr1 = [1, 5 , 11 ,5]
    print("should be true: {}".format(eq_subsets(test_arr1)))

    test_arr2 = [1, 3, 5]
    print("should be false: {}".format(eq_subsets(test_arr2)))

    test_arr3 = [3, 1, 5, 9, 12]
    print("should be true: {}".format(eq_subsets(test_arr3)))

    test_arr4 = [10, 7, 4, 8]
    print("should be false: {}".format(eq_subsets(test_arr4)))
    
    test_arr5 = [4, 5, 1, 11, 10, 3]
    print("should be true: {}".format(eq_subsets(test_arr5)))

    test_arr6 = [4, 5, 6, 11, 120, 4]
    print("should be false: {}".format(eq_subsets(test_arr6)))