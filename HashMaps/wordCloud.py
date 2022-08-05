import re


def wordCloud(input):
    """
        Args:
            input: a string
        Returns:
            dictionary representing the word cloud
    """
    # turn all letters into lowercase
    input = input.lower()
    # remove all punctuation characters
    # ^: not, \w: alphanumeric character, \s: whitespace
    input = re.sub(r'[^\w\s-]', '', input)
    map = {}
    for i in input.split(' '):
        map[i] = map.setdefault(i, 0) + 1
    return map


if __name__ == '__main__':
    input = "'After beating the eggs, Dana read the next-step:' 'Add milk and eggs, then add flour and sugar.'"
    print(wordCloud(input))
    input = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake. 'The bill came to five dollars.'"
    print(wordCloud(input))
