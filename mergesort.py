def mergesort(l):
    n = len(l)
    if n > 1:
        mid = n//2
        left = mergesort(l[:mid])
        right = mergesort(l[mid:])

        l = []
        while left and right:
            if left[0] < right[0]:
                l.append(left.pop(0))
            else:
                l.append(right.pop(0))

        for e in left:
            l.append(e)
        for e in right:
            l.append(e)

    return l

newlist = [5,2,7,2,23,6,2,453,43,65]
print(mergesort(newlist))