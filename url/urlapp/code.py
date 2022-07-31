def base4(num):
    st=list("0000")
    i=3
    while(num):
        st[i]=str(num%4)
        num=int(num/4)
        i=i-1
    return "".join(st)

def g_shorturl(index):
    characters="abcd"
    st=""
    codevalue=base4(index)
    for i in codevalue:
        st=st+characters[int(i)]
    return st
