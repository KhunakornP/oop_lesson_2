import copy
def gen_comb_list(list_set):
    """
        Parameters:
            list_set: a list of lists where each contains at least one element

        Returns:
            a list of lists, each of which is made from a combination of elements in each list in list_set

        Examples:
            gen_comb_list([[1, 2, 3]]) returns [[1], [2], [3]]
            gen_comb_list([[1, 2, 3], [4, 5]]) returns [[1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5]]
            gen_comb_list([[1, 2, 3], [4, 5], [6, 7, 8]]) returns [[1, 4, 6], [2, 4, 6], [3, 4, 6], [1, 5, 6], [2, 5, 6], [3, 5, 6], [1, 4, 7], [2, 4, 7], [3, 4, 7], [1, 5, 7], [2, 5, 7], [3, 5, 7], [1, 4, 8], [2, 4, 8], [3, 4, 8], [1, 5, 8], [2, 5, 8], [3, 5, 8]]
    """
    if len(list_set) == 1:
        _list = []
        for i in list_set[0]:
            _list.append([i])
        return _list
    if list_set[0] != list:
        temp_list = []
        for i in list_set[0]:
            for j in list_set[1]:
                temp_list.append([i,j])
        list_set.pop(0)
        list_set.pop(0)
        list_set.insert(0, temp_list)
    if len(list_set) >= 2:
        temp_list = []
        for i in list_set[0]:
            for j in list_set[1]:
                x = copy.deepcopy(i)
                x.append(j)
                temp_list.append(x)
        list_set.pop(0)
        list_set.pop(0)
        list_set.insert(0, temp_list)
        gen_comb_list(list_set)
    return list_set[0]


print(gen_comb_list([[1, 2, 3]]))
print(gen_comb_list([[1, 2, 3], [4, 5]]))
print(gen_comb_list([[1, 2, 3], [4, 5], [6, 7, 8]]))