# coding= utf-8


sum=0
i=0
while i <=100:
    sum+=i
    i+=1
print("1到100的和：%d" %sum )



a= input("shuru")
try:
    3/a
except Exception as error:
    print(error)