from audioop import reverse


def reverseCharacters(message, l, r):
    while l < r:
        message[l], message[r] = message[r], message[l]
        l += 1
        r -= 1


def reverseWords(message):
    """
        Args:
            A list of words
            message = [ 'c', 'a', 'k', 'e', ' ',
                        'p', 'o', 'u', 'n', 'd', ' ',
                        's', 't', 'e', 'a', 'l' ]
        Returns:
            A reversed list of the original message with in-word order preserved
            'steal pound cake'
        Time complexity: O(n)
        Space complexity: O(1)
    """
    # reverse all characters
    # within each word, reverse the characters again
    reverseCharacters(message, 0, len(message)-1)
    message.append(' ')
    prev = -1
    i = 0
    while i < len(message):
        if message[i] == ' ':
            reverseCharacters(message, prev+1, i-1)
            prev = i
        i += 1
    return ''.join(message)


if __name__ == '__main__':
    message = ['c', 'a', 'k', 'e', ' ',
               'p', 'o', 'u', 'n', 'd', ' ',
               's', 't', 'e', 'a', 'l']
    print(reverseWords(message))
