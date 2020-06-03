css = ['零','一','二','三','四','五','六','七','八','九']
a = input()
i=0
lena=len(a)
for k in range(lena):
    b=int(a[i])
    print(css[b],end='')
    i=i+1