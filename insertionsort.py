def insertionsort(unordered_list):
    for k in range(len(unordered_list)):
        for i in range (1, len(unordered_list)):
            if(unordered_list[i] < unordered_list[i-1]):
                j = i-1
                while j > 0 and unordered_list[j] < unordered_list[i]:
                    j -= 1
                hold = unordered_list[i]
                for x in range(i, j, -1):
                    unordered_list[x] = unordered_list[x-1]
                unordered_list[j] = hold
    return unordered_list

print(insertionsort([4,1,8,12,6,2]))