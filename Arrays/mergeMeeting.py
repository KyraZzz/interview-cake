def mergeMeeting(rangeTuple):
    """
    Args:
        rangeTuple(list): A list of multiple meeting time ranges
        [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    Returns:
        list: condensed ranges
        [(0, 1), (3, 8), (9, 12)]
    Time Complexity: O(nlogn)
    """
    # sort the list of tuples based on the starting time
    # for each adjacent tuples, figure out whether they overlap snd.start <= fst.end
    # merge tuples iteratively
    sorted_list = sorted(rangeTuple, key=lambda x: x[0])
    i = 0
    while i < len(sorted_list) - 1:
        if sorted_list[i][1] >= sorted_list[i+1][0]:
            sorted_list[i] = (sorted_list[i][0], sorted_list[i+1][1])
            sorted_list.pop(i+1)
        else:
            i += 1

    return sorted_list


if __name__ == "__main__":
    tuples = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    print(mergeMeeting(tuples))
