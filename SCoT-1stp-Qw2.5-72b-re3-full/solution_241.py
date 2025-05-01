def array_3d(m, n, o):
    result = []
    for i in range(m):
        layer = []
        for j in range(n):
            row = []
            for k in range(o):
                row.append('*')
            layer.append(row)
        result.append(layer)
    return result