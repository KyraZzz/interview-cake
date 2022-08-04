def mergeSortedArray(l1, l2):
    """
        Args:
            l1 : a list of sorted numbers
            l2 : a list of sorted numbers
        Returns:
            a merged list of sorted numbers, combining l1 and l2
        Time complexity: O(n)
        Space complexity: O(n)
    """
    p1 = 0
    p2 = 0
    l = []
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] <= l2[p2]:
            l.append(l1[p1])
            p1 += 1
        else:
            l.append(l2[p2])
            p2 += 1
    if p1 < len(l1) - 1:
        l.extend(l1[p1:])
    if p2 < len(l2) - 1:
        l.extend(l2[p2:])
    return l


if __name__ == '__main__':
    my_list = [3, 4, 6, 10, 11, 14]
    alices_list = [1, 5, 8, 12, 15, 19]

    # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    print(mergeSortedArray(my_list, alices_list))
