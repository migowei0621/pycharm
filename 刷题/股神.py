while 1:
    s = raw_input()
    if s != "":
        n = int(s)-1
        val = 1
        up = 1
        while n >= up + 1:
            val = val + up -1
            n = n - 1 - up
            up += 1
        val = val + n
        print val
