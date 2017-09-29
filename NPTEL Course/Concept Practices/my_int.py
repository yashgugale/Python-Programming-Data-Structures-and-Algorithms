def my_int(s, b = 10):
    if b == 2:
        return(int(s,2))
    if b == 8:
        return(int(s,8))
    if b == 16:
        return(int(s,16))
    else:
        return(int(s))

print(my_int("1001", 8))
