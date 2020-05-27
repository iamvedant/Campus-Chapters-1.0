# cook your dish here
try:
    t=int(input())
    while(t):
        n=int(input())
        l=list(map(int,input().split()))
        m=list(map(int,input().split()))
        if((max(l)>max(m))or(max(m)>max(l))):
            print("YES")
        else:
            print("NO")
        t-=1
except:
    pass
