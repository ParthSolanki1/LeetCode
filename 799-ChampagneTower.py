def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    i = 0
    j = 0
    row = []
    prev_row = []

    while(i < query_row or (i == query_row and j <= query_glass)):
        if(prev_row == []):
            row.append(poured)
            current = poured
        else:
            if(j == 0):
                volLeft = (prev_row[0] - 1)/2
            elif(j == i):
                volLeft = (prev_row[j-1] - 1)/2
            else:
                left = (prev_row[j-1] - 1) / 2
                right = (prev_row[j] - 1) / 2

                if(left > 0 and right > 0):
                    volLeft = left + right
                elif(left > 0):
                    volLeft = left
                elif(right > 0):
                    volLeft = right
                else:
                    volLeft = 0

            row.append(volLeft if volLeft > 0 else 0)

            current = row[j]
        
        if(len(row) == i+1):
            prev_row = row[:]
            row = []
        
        if(j < i):
            j += 1
        else:
            i += 1
            j = 0
    
    return current if current < 1 else 1


print(champagneTower(6, 3, 1))