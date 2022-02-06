# Output:   if odd, return Weird,
#           if even and in range 2,5 return Not Weird,
#           if even and in range 6,20 return Weird,
#           if even and over 20, return Not Weird

def weird_number():
    n = input("Write a number to see if it's weird: ")
    weird = "Weird"
    not_weird = "Not Weird"
    n = int(n)
    if n % 2 != 0:
        print(weird)
    else:
        if 2 <= n <= 5:
            print(not_weird)
        elif 6 <= n <= 20:
            print(weird)
        else:
            print(not_weird)
