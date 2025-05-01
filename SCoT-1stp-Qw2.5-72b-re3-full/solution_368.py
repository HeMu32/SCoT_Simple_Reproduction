def repeat_tuples(test_tup, N):
    if N < 1:
        return ()
    else:
        result = test_tup * N
        return result