import copy


def merge(lst1, lst2):
    """
    (list,list) -> list
    function return one sorted list of two lists
    >>>merge([1,3],[2,4])
    [1,2,3,4]
    >>>merge([1,3,5],[1,2,6])
    [1,1,3,5,6]
    """
    i1 = 0
    i2 = 0
    newlst = []
    while (i1 != len(lst1)) and (i2 != len(lst2)):
        if lst1[i1] < lst2[i2]:
            newlst.append(lst1[i1])
            i1 += 1
        else:
            newlst.append(lst2[i2])
            i2 += 1
    newlst.extend(lst1[i1:])
    newlst.extend(lst2[i2:])
    return newlst


def mergesort(lst):
    """
    (list) -> list
    function return sorted list
    >>>mergesort([1,2,3,4,5])
    [1,2,3,4,5]
    >>>mergesort([])
    []
    >>>mergesort([5,7,1,3,-1])
    [-1,1,4,5,7]
    """
    workspace = []
    for i in range(len(lst)):
        workspace.append([lst[i]])
        if type(lst[i]) == str:
            raise ValueError
    i = 0
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        new_lst = merge(L1, L2)
        workspace.append(new_lst)
        i = i + 2
    if len(workspace) != 0:
        lst[:] = workspace[-1][:]
    return lst


def is_sorted(lst):
    """
    (lst) -> bool
    check if list is sorted
    :return:
    """
    start_lst = copy.deepcopy(lst)
    sorted_lst = mergesort(lst)
    return sorted_lst == start_lst
