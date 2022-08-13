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
    for i in range(2, len(list_of_ints)-1):
        current = list_of_ints[i]
        high_prod_three = max(high_prod_three, current * high_prod_two)
        high_prod_two = max(high_prod_two, current * high)
        high = max(high, current)
        low_prod_two = min(low_prod_two, current * low, current * high)
        low = min(low, current)
    return max(list_of_ints[-1] * low_prod_two, list_of_ints[-1] * high_prod_two)


if __name__ == '__main__':
    list = [10, 7, -5, 8, -11, 9, -100]
    print(highestProductOfThree(list))
