def line_intersect(lst_first, lst_second):
    """
    function that search ntersect of two lines
    :param lst_first: lst
    :param lst_second: lst
    :return: None or lst or tuple
    """
    x_1 = lst_first[0][0]
    x_2 = lst_first[1][0]
    y_1 = lst_first[0][1]
    y_2 = lst_first[1][1]
    try:
        k_1 = (y_1 - y_2)/(x_1 - x_2)
    except ZeroDivisionError:
        k_1 = 0
    try:
        B_1 = (y_1 - x_1 * k_1)
    except ZeroDivisionError:
        B_1 = 0
    x_1 = lst_second[0][0]
    x_2 = lst_second[1][0]
    y_1 = lst_second[0][1]
    y_2 = lst_second[1][1]
    try:
        k_2 = (y_1 - y_2) / (x_1 - x_2)
    except ZeroDivisionError:
        k_2 = 0
    try:
        B_2 = (y_1 - x_1 * k_2)
    except ZeroDivisionError:
        B_2 = 0
    if k_1 == k_2 and B_1 == B_2:
        return lst_first
    try:
        intersect_x = (B_2 - B_1) / (k_1 - k_2)
        intersect_y = intersect_x * k_1 + B_1
    except ZeroDivisionError:
        return None
    else:
        return (intersect_x, intersect_y)

