def utopianTree(n):
    height = 1
    for cycle in range(n+1):
        if cycle==0:
            height = 1
        elif (cycle % 2) != 0:
            height = height*2
        else:
            height = height+1
    return height
