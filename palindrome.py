def pal(n):
    if len(n)<=1:
        return True
    if n[0]==n[-1]:
        return pal(n[-1:1])
    else:
        return False
