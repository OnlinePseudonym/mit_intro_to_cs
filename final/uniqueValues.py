def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    value_dict = {}
    result = []
    if aDict == {}:
        return result
    for e in aDict:
        if aDict[e] in value_dict:
            value_dict[aDict[e]] += 1
        else:
            value_dict[aDict[e]] = 1
    dict_copy = value_dict.copy()
    for e in dict_copy:
        if value_dict[e] != 1:
            del value_dict[e]
    for e in aDict:
        if aDict[e] in value_dict:
            result.append(e)
    result = sorted(result)
    return result

aDict = {1: 1, 2: 1, 3: 1}
print(uniqueValues(aDict))