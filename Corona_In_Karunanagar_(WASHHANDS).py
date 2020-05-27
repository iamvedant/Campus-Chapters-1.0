# cook your dish here
try:
    t=int(input())
    while(t):
        n=int(input())
        s=input()
        l=list(map(int,s))
        v=[0]*n
        m=[]
        for i in range(n):
            if(l[i]==1):
                m.append(i+1)
        x=int(input())
        f=list(map(int,input().split()))
        for i in range(x):
            if(l[f[i]-2]==1):
                v[f[i]-2]=-1
            elif(l[f[i]-2]==0):
                v[f[i]-2]=-2
            y=[]
            for j in range(len(m)):
                if(m[j]-2>=0):
                    if((l[m[j]-2]==0) and (v[m[j]-2]>=0)):
                        y.append(m[j]-1)
                        l[m[j]-2]=1
                if(m[j]<n):
                    if((l[m[j]]==0) and (v[m[j]-1]>=0)):
                        y.append(m[j]+1)
                        l[m[j]]=1
                if(m[j]<n):
                    if((l[m[j]]==0) and(v[m[j]]==-2)):
                        y.append(m[j]+1)
                        l[m[j]]=1
                        v[m[j]]=-1
            m=[]
            m.extend(y)
        print(l.count(1))
        t-=1
except:
    pass
