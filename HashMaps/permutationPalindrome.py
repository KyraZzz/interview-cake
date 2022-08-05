def permutationPalindrome(input):
    """
        Args: 
            input: a string
        Returns:
            bool: whether the input string is a palindrome
    """
    seenOdd = set()
    for i in input:
        if i in seenOdd:
            seenOdd.remove(i)
        else:
            seenOdd.add(i)
    return len(seenOdd) <= 1


if __name__ == '__main__':
    print(permutationPalindrome("civic"))
    print(permutationPalindrome("ivicc"))
    print(permutationPalindrome("civil"))
    print(permutationPalindrome("livci"))
