def list_split(S, step):
    result = []
    for i in range(step):
        temp = []
        for j in range(i, len(S), step):
            temp.append(S[j])
        result.append(temp)
    return result