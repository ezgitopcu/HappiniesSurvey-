import numpy as np

loc='ACME-HappinessSurvey2020.csv'
b=[]
mults=[10,40,15,2,30,3]
with open(loc) as file:
    a=file.readlines()
    for i in range(len(a)):
        temp=a[i].split(',')
        tempList = []
        for j in range (len(temp)):

            if j==len(temp)-1:
                tempValue=temp[j].split('\n')
                tempList.append(tempValue[0])
            else:
                tempList.append(temp[j])
        b.append(tempList)




happyCount=0
RealHappyCount=0
FalseHappyCount=0
FalseSadCount=0
for temp in range(len(b)-1):
    i=temp+1
    PersonTempHappines=0
    for j in range(len(b[i])-1):
        PersonTempHappines+=int(b[i][j+1])*mults[j]
    PersonHappines=PersonTempHappines/120


    if PersonHappines>=2.5:
       print("Customer "+str(i)+" is Happy: "+str(PersonHappines)+" RealHappiness:"+str(b[i][0]))
       happyCount+=1
       if(int(b[i][0])==1):
           RealHappyCount+=1
       else:
           FalseHappyCount+=1

    else:
        print("Customer "+str(i)+" is Not Happy: "+str(PersonHappines)+" RealHappiness:"+str(b[i][0]))

        if int(b[i][0])==1:
            RealHappyCount += 1
            FalseSadCount += 1

print("HappyCount:"+str(happyCount))


print("RealHappyCount:"+str(RealHappyCount))
print("FalseHappyCount:"+str(FalseHappyCount))
print("FalseSadCount:"+str(FalseSadCount))
tempHappy=RealHappyCount*100/happyCount

if tempHappy>100:
    tempHappy=200-tempHappy
if tempHappy<=0:
    tempHappy=0
print(tempHappy)