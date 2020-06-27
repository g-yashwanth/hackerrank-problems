def beautifulDays(i, j, k):
    beautiful = 0
    for day in range(i,j+1):
        if (day-(int(str(day)[::-1])))>=0:
            if (day-(int(str(day)[::-1])))%k==0:
                beautiful = beautiful+1
        else:
            if ((int(str(day)[::-1]))-day)%k==0:
                beautiful = beautiful+1
    return beautiful
