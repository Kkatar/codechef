# cook your dish here
a,b=map(int,input().split())
if 1<=a<180 and 1<=b<180 and a+b<180:
    print(180-(a+b))