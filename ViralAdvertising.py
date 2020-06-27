def viralAdvertising(n):
    people = 5
    liked = 0
    for day in range(n):
        liked = liked + (people//2)
        people = (people//2)*3
    return liked
