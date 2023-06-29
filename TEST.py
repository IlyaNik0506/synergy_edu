def min_cuts(N):
    if N % 2 == 0:
        return N
    else:
        return N + 1


N = int(input())
min_cuts_required = min_cuts(N)
print(min_cuts_required)
