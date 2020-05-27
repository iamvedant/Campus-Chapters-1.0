# cook your dish here
try:
    import math as mt
    def great(a,b):
        if(a>=b):
            return a
        else:
            return b
    t=int(input())
    while(t):
        a,b=map(int,input().split())
        g=great(a,b)
        power=int((mt.log(g)/mt.log(2)))+1
        mx=a^b
        
        rotation=0
        mx_rotation=0
        for i in range(1,power):
            end=b&1
            b=b>>1
            b=b|int((end*(2**(power-1))))
            rotation+=1
            if((a^b)>mx):
                mx=a^b
                mx_rotation=rotation
        # print(power)
        # print(mx)
        print(mx_rotation,mx)
        t-=1
except:
    pass
