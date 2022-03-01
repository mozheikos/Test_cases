def fibonacci(q):

    f_1 = 0
    f_2 = 1
    result = [0]
    count = 1
    # Using count instead of len(result) because len(result) - is a function,
    # which will call every loop. If q-argument will big enough - efficiency
    # will decline
    while count < q:
        f = f_1 + f_2
        # for even-detect using property of binary system: last bit of even
        # number always equal to 0. When using binary "and", in result, every
        # bit equal to 1 only when same bit of both arguments equal to 1.
        # So, 1 in binary system is 0000 0001, in this way, result of operation
        # "binary and" between any even number and 1 will equal to 0
        if f & 1 == 0:
            result.append(f)
            count += 1
        f_1 = f_2
        f_2 = f
    return result


print(fibonacci(6))
