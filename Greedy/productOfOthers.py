import numpy as np


def productOfOthers(l):
    """
        Args: 
            l: a list of integers
        Returns:
            a list of products
        Time complexity: O(n)
        Space complexity: O(n)
    """
    if len(l) < 2:
        return
    prefix = np.cumprod(l)
    suffix = np.cumprod(l[::-1])
    suffix = suffix[::-1]
    product = [None] * len(l)
    for i in range(len(l)):
        if i - 1 >= 0 and i + 1 < len(l):
            product[i] = prefix[i-1] * suffix[i+1]
        elif i == 0:
            product[i] = suffix[i+1]
        else:
            product[i] = prefix[i-1]
    return product


if __name__ == '__main__':
    l = [1, 3, 4, 5, 2]
    print(productOfOthers(l))
