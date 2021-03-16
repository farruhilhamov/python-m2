t = "<dec0ring>"
s = 0
l = len(t)
while True:
    for i in t:
        text = t [s:s+len(t):]
        other = t [l::]
        s +=1
        l -= 1
        if l == 0:
            s = 0
            l = len(t)
        print(text+other)
