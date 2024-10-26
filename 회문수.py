def palindrome(s):
    c = 1
    i = 1

    while True:
        w = str(i)
        palindrom = int(w + w[-2::-1]) if len(w) > 1 else i

        if palindrom >= s:
            break

        c += 1
        i += 1
    return c


n = int(input())
print(palindrome(n))