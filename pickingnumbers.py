def pickingNumbers(a):
    # Write your code here
    a.sort()
    large = 0
    largest = 0
    for no in a:
        if a.count(no-1) + a.count(no) > a.count(no)+a.count(no+1):
            large = a.count(no-1) + a.count(no)
        else:
            large = a.count(no) + a.count(no+1)
        if large > largest:
            largest = large
    return largest
