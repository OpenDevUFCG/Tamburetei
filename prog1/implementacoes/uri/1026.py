while True:
    try:
        a, b = [int(x) for x in input().strip().split(' ')]
        print(a ^ b)
    except EOFError:
        break