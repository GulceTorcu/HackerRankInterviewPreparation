# Output: if the year n is leap year,
#        if evenly divided by 4, yes, if evenly divided by 100 no, if evenly divided by 400 yes


def is_leap():
    n = int(input("Year: "))
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False
