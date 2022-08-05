from math import inf


def inflights(flight_length, movie_lengths):
    """
        Args:
            flight_length: an integer (minutes)
            movie_lengths: a list of integers (minutes)
        Returns:
            bool: whether there are two numbers in movie+lengths whose sum equals flight_length
    """
    seen = set()
    for v in movie_lengths:
        remain = flight_length - v
        if v in seen:
            return True
        seen.add(remain)
    return False


if __name__ == '__main__':
    flight_length = 8
    movie_lengths = [1, 4, 2, 4, 3]
    print(inflights(flight_length, movie_lengths))
