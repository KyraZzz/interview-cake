def highestProductOfThree(list_of_ints):
    """
        Args:
            list_of_ints: len >= 3, integer range (positive & negative)
        Returns:
            integer representing the highest product of three integers
        Time complexity: O(n)
    """
    # two possible cases: (1) 3 positive integers, (2) 1 positive integer and 2 negative integers
    high = max(list_of_ints[0], list_of_ints[1])
    high_prod_two = list_of_ints[0] * list_of_ints[1]
    high_prod_three = high_prod_two * list_of_ints[2]
    low = min(list_of_ints[0], list_of_ints[1])
    low_prod_two = high_prod_two
    low_prod_three = high_prod_three
    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]
        high_prod_three = max(high_prod_three, current * high_prod_two)
        high_prod_two = max(high_prod_two, current * high)
        high = max(high, current)
        low_prod_three = min(low_prod_three, current * low_prod_two)
        low_prod_two = min(low_prod_two, current * low)
        low = min(low, current)
    return high_prod_three


if __name__ == '__main__':
    list = [-10, -10, 1, 3, 2]
    print(highestProductOfThree(list))
