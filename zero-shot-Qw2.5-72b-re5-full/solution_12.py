def sort_matrix(M):
    """
    Write a function to sort a given matrix in ascending order according to the sum of its rows.
    """
    M.sort(key=sum)
    return M