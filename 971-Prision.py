def prisonAfterNDays(cells, N):
    cycle = []

    if(N == 0):
        return cells

    i = 0
    temp = [0,] + cells[1:7] + [0,]
    while(i <= N):
        if(cells not in cycle):
            cycle.append(cells)

            for j in range(1, 7):
                if(cells[j-1] == cells[j+1]):
                    temp[j] = 1
                else:
                    temp[j] = 0

            cells = temp[:]

            i += 1
        else:
            k = cycle.index(cells)
            cycle = cycle[k:]
            break

    return cycle[((N - i) % len(cycle))]

print(prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))