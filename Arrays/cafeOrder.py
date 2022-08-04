def cafeOrder(to_order, di_order, serve):
    """
        Args:
            to_order: a list of take out orders
            di_order: a list of dine in orders
            serve: a list of serve orders
        Returns:
            bool: whether serve order in FIFO
    """
    p1 = 0
    p2 = 0
    p3 = 0
    while p1 <= len(to_order) and p2 <= len(di_order) and p3 < len(serve):
        if p1 < len(to_order) and serve[p3] == to_order[p1]:
            p1 += 1
        elif p2 < len(di_order) and serve[p3] == di_order[p2]:
            p2 += 1
        else:
            return False
        p3 += 1
    return True


if __name__ == "__main__":
    to_order = [1, 3, 5]
    di_order = [2, 4, 6]
    serve = [1, 2, 4, 6, 5, 3]
    print(cafeOrder(to_order, di_order, serve))
    to_order = [17, 8, 24]
    di_order = [12, 19, 2]
    serve = [17, 8, 12, 19, 24, 2]
    print(cafeOrder(to_order, di_order, serve))
