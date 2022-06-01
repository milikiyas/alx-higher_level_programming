k = ord('a')
while k <= 122:
    if not(k == 101 or k == 113):
        ch = chr(k)
        print('{}'.format(ch), end="")
        k += 1
    elif k == 101 or k == 113:
        k += 1
