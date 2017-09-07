txt = 'map'
res = []
res_str = ''
for i in range(len(txt)):
    if txt[i] == 'y':
        res.append('a')
    elif txt[i] == 'z':
        res.append('b')
    elif txt[i].isalpha():
        res.append(chr(ord(txt[i])+2))
    else:
        res.append(txt[i])
print(res_str.join(res))
