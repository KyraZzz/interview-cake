import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling+1)


def inplaceShuffle(l):
    """
        Fisher-Yates shuffle or Knuth shuffle
        Args:
            l: a list
        Returns:
            A random uniform shuffle of the list l
    """
    # each time randomly select one number from the remaining i numbers
    # swap that with i-1(th) number in the list l inplace
    if len(l) < 1:
        return l
    for i in range(len(l)):
        ind = get_random(i, len(l) - 1)
        l[i], l[ind] = l[ind], l[i]
    return l


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(inplaceShuffle(l))
