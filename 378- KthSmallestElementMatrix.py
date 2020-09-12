def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    i = 0
    j = 0

    while i <= n and j <= n:
        if(i <= j):
            