try:
    t=int(input())
    while(t):
        time=0
        m,n=map(int,input().split())
        l=[]
        for i in range(0,m):
            f=list(map(str,input().split()))
            l.append(f)
        x=[]
            
        for i in range(0,m):
            if((i+1)%2==0):
                for j in range(n-1,-1,-1):
                    if(l[i][j]=='P'):
                        y=[]
                        y.append(i+1)
                        y.append(j+1)
                        x.append(y)
            else:
                for j in range(0,n):
                    if(l[i][j]=='P'):
                        y=[]
                        y.append(i+1)
                        y.append(j+1)
                        x.append(y)
        if(x==[] or len(x)==1):
            t=0
        else:
            for i in range(1,len(x)):
                time=time+abs(x[i][0]-x[i-1][0])
                time=time+abs(x[i][1]-x[i-1][1])
        print(time)
        t-=1
except:
    pass
