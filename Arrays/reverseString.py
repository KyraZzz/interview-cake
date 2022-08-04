def reverseString(character_list):
    """
        Args:
            A list of characters
        Returns:
            A reversed list of the original character list
        Time complexity: O(n)
        Space complexity: O(1)
    """
    # Using two pointers, one at the start, one at the end
    p1 = 0
    p2 = len(character_list) - 1
    while p1 < p2:
        character_list[p1], character_list[p2] = character_list[p2], character_list[p1]
        p1 += 1
        p2 -= 1
    return character_list


if __name__ == '__main__':
    character_list = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print(reverseString(character_list))
