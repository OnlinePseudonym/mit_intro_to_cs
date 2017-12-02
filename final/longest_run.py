def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    longest_list = []
    longest_inc = []
    longest_dec = []
    cur_list = []
    cur_int = 0
    result = 0

    for e in L:
        if len(cur_list) < 1:
            cur_list.append(e)
            cur_int = e
        else:
            if e >= cur_int:
                cur_list.append(e)
                cur_int = e
            else:
                if len(cur_list) > len(longest_inc):
                    longest_inc = cur_list
                cur_list = []
                cur_list.append(e)
                cur_int = e
    if len(cur_list) > len(longest_inc):
        longest_inc = cur_list
    cur_list = []
    for e in L:
        if len(cur_list) < 1:
            cur_list.append(e)
            cur_int = e
        else:
            if e <= cur_int:
                print(cur_int)
                cur_list.append(e)
                cur_int = e
            else:
                if len(cur_list) > len(longest_dec):
                    longest_dec = cur_list
                cur_list = []
                cur_list.append(e)
                cur_int = e
    if len(cur_list) > len(longest_inc):
        longest_inc = cur_list
    print(longest_dec)
    print(longest_inc)
    if len(longest_dec) == len(longest_inc):
        def list_index(list, sublist):
            """return index of sublist"""
            for ind in (i for i,e in enumerate(list) if e == sublist[0]):
                if list[ind:ind+len(sublist)] == sublist:
                    return ind
        dec_ind = list_index(L, longest_dec)
        inc_ind = list_index(L, longest_inc)
        if dec_ind < inc_ind:
            for e in longest_dec:
                result += e
        else:
            for e in longest_inc:
                result += e
    elif len(longest_dec) > len(longest_inc):
        for e in longest_dec:
            result += e
    else:
        for e in longest_inc:
            result += e
    return result

L = [1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(longest_run(L))